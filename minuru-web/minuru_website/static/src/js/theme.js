/** @odoo-module **/

(function init() {
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
        return;
    }
    if (!document.querySelector('.mn-wrap')) return;

    // ── Scroll container ─────────────────────────────────────
    const scrollEl = (function () {
        const ww = document.getElementById('wrapwrap');
        if (ww) return ww;
        document.body.scrollTop = 1;
        if (document.body.scrollTop > 0) { document.body.scrollTop = 0; return document.body; }
        return document.documentElement;
    })();
    function getScrollY() { return scrollEl.scrollTop; }

    // ── Navbar ───────────────────────────────────────────────
    const navbar = document.getElementById('mn-navbar');
    if (navbar) {
        let lastY = getScrollY();
        function handleNav() {
            const y    = getScrollY();
            const diff = y - lastY;
            if (y <= navbar.offsetHeight) {
                navbar.classList.remove('mn-nav-hidden');
            } else if (diff > 4) {
                navbar.classList.add('mn-nav-hidden');
            } else if (diff < -4) {
                navbar.classList.remove('mn-nav-hidden');
            }
            navbar.classList.toggle('scrolled', y > 60);
            lastY = y;
        }
        scrollEl.addEventListener('scroll', handleNav, { passive: true });
        window.addEventListener('scroll',   handleNav, { passive: true });
        handleNav();
    }

    // ── Hero video autoplay fallback ─────────────────────────
    const heroVideo = document.querySelector('.mn-hero-bg');
    if (heroVideo && heroVideo.tagName === 'VIDEO') {
        heroVideo.play().catch(() => {});
    }

    // ── Mobile menu ──────────────────────────────────────────
    const hamburger   = document.getElementById('mn-hamburger');
    const mobileMenu  = document.getElementById('mn-mobile-menu');
    const mobileClose = document.getElementById('mn-mobile-close');

    function closeMobile() {
        if (!mobileMenu) return;
        mobileMenu.classList.remove('open');
        // Only restore scroll if the modal is also not open
        const modalBackdrop = document.getElementById('mn-modal-backdrop');
        if (!modalBackdrop || !modalBackdrop.classList.contains('open')) {
            document.body.style.overflow = '';
            scrollEl.style.overflow = '';
        }
    }
    if (hamburger && mobileMenu) {
        hamburger.addEventListener('click', function () {
            const open = mobileMenu.classList.toggle('open');
            document.body.style.overflow = open ? 'hidden' : '';
            scrollEl.style.overflow      = open ? 'hidden' : '';
        });
    }
    if (mobileClose) mobileClose.addEventListener('click', closeMobile);

    // ── Logo → scroll to top ─────────────────────────────────
    document.addEventListener('click', function (e) {
        const logo = e.target.closest('.mn-nav-logo');
        if (!logo) return;
        e.preventDefault();
        try { scrollEl.scrollTo({ top: 0, behavior: 'smooth' }); }
        catch (_) { window.scrollTo({ top: 0, behavior: 'smooth' }); }
    }, true);

    // ── Smooth scroll (hash links + /#hash links) ────────────
    function smoothScrollToHash(hash) {
        if (!hash || hash === '#') return false;
        // Normalise: strip leading /
        const id = hash.replace(/^\//, '');
        const target = document.querySelector(id);
        if (!target) return false;
        const offset = (navbar ? navbar.offsetHeight : 0) + 16;
        const cRect  = scrollEl.getBoundingClientRect ? scrollEl.getBoundingClientRect().top : 0;
        const tRect  = target.getBoundingClientRect().top;
        const top    = getScrollY() + (tRect - cRect) - offset;
        try { scrollEl.scrollTo({ top, behavior: 'smooth' }); }
        catch (_) { window.scrollTo({ top, behavior: 'smooth' }); }
        return true;
    }

    document.addEventListener('click', function (e) {
        // Plain hash links: href="#section"
        const hashLink = e.target.closest('a[href^="#"]');
        if (hashLink) {
            const href = hashLink.getAttribute('href');
            if (!href || href === '#') return;
            if (!smoothScrollToHash(href)) return;
            e.preventDefault();
            e.stopPropagation();
            closeMobile();
            return;
        }
        // Root-relative hash links: href="/#section" (mobile menu)
        const rootHashLink = e.target.closest('a[href^="/#"]');
        if (rootHashLink) {
            const href = rootHashLink.getAttribute('href');       // e.g. "/#routes"
            const hash = href.replace(/^\//, '');                 // → "#routes"
            if (!smoothScrollToHash(hash)) return;
            e.preventDefault();
            e.stopPropagation();
            closeMobile();
        }
    }, true);

    // ── Reveal ───────────────────────────────────────────────
    const revealEls = document.querySelectorAll('.mn-reveal');
    if (revealEls.length) {
        const obs = new IntersectionObserver(function (entries) {
            entries.forEach(function (e) {
                if (e.isIntersecting) { e.target.classList.add('visible'); obs.unobserve(e.target); }
            });
        }, {
            threshold: 0.07,
            root: scrollEl === document.documentElement ? null : scrollEl,
        });
        revealEls.forEach(function (el) { obs.observe(el); });
        document.body.classList.add('mn-ready');
    }

    // ── Language toggle ──────────────────────────────────────
    const langBtns = document.querySelectorAll('.mn-lang-btn');
    function setLang(lang) {
        document.body.classList.toggle('mn-lang-mn', lang === 'mn');
        langBtns.forEach(function (b) { b.classList.toggle('active', b.dataset.lang === lang); });
        try { localStorage.setItem('mn-lang', lang); } catch (_) {}
    }
    let savedLang = 'en';
    try { savedLang = localStorage.getItem('mn-lang') || 'en'; } catch (_) {}
    setLang(savedLang);
    langBtns.forEach(function (b) { b.addEventListener('click', function () { setLang(b.dataset.lang); }); });

    // ── Floating CTA ─────────────────────────────────────────
    const fab = document.getElementById('mn-fab');
    if (fab) {
        const heroEl = document.querySelector('.mn-hero');
        function updateFab() {
            const threshold = heroEl ? heroEl.offsetHeight * 0.8 : window.innerHeight;
            fab.classList.toggle('mn-fab-visible', getScrollY() > threshold);
        }
        scrollEl.addEventListener('scroll', updateFab, { passive: true });
        window.addEventListener('scroll',   updateFab, { passive: true });
        updateFab();
    }

    // ── Stat counters ────────────────────────────────────────
    const countEls = document.querySelectorAll('[data-count]');
    if (countEls.length) {
        function fmt(val, el) {
            const suf = el.dataset.suffix || '';
            if (val >= 1000000) {
                const m = val / 1000000;
                return (Number.isInteger(m) ? m : m.toFixed(1)) + 'M' + suf;
            }
            return Math.round(val) + suf;
        }
        function runCounter(el) {
            const target = +el.dataset.count;
            const dur    = 1400;
            let start    = null;
            (function step(ts) {
                if (!start) start = ts;
                const p = Math.min((ts - start) / dur, 1);
                const e = 1 - Math.pow(1 - p, 3);
                el.textContent = fmt(target * e, el);
                if (p < 1) requestAnimationFrame(step);
                else el.textContent = fmt(target, el);
            })(performance.now());
        }
        const cobs = new IntersectionObserver(function (entries) {
            entries.forEach(function (e) {
                if (e.isIntersecting) { runCounter(e.target); cobs.unobserve(e.target); }
            });
        }, { threshold: 0.5, root: scrollEl === document.documentElement ? null : scrollEl });
        countEls.forEach(function (el) { cobs.observe(el); });
    }

    // ── Fleet photo slider ──────────────────────────────────
    document.querySelectorAll('[data-fleet-slider]').forEach(function (slider) {
        const slides = Array.from(slider.querySelectorAll('.mn-fleet-slide'));
        const dots = Array.from(slider.querySelectorAll('[data-fleet-dot]'));
        const prev = slider.querySelector('[data-fleet-prev]');
        const next = slider.querySelector('[data-fleet-next]');
        if (!slides.length) return;

        let active = slides.findIndex(function (slide) { return slide.classList.contains('active'); });
        if (active < 0) active = 0;
        let autoTimer = null;

        function show(index) {
            active = (index + slides.length) % slides.length;
            slides.forEach(function (slide, i) { slide.classList.toggle('active', i === active); });
            dots.forEach(function (dot, i) { dot.classList.toggle('active', i === active); });
        }

        function startAuto() {
            stopAuto();
            autoTimer = setInterval(function () { show(active + 1); }, 3800);
        }

        function stopAuto() {
            if (autoTimer) { clearInterval(autoTimer); autoTimer = null; }
        }

        if (prev) prev.addEventListener('click', function () { show(active - 1); stopAuto(); });
        if (next) next.addEventListener('click', function () { show(active + 1); stopAuto(); });
        dots.forEach(function (dot) {
            dot.addEventListener('click', function () { show(+dot.dataset.fleetDot || 0); stopAuto(); });
        });

        // Pause on hover, resume on leave
        slider.addEventListener('mouseenter', stopAuto);
        slider.addEventListener('mouseleave', startAuto);

        // Pause when tab not visible
        document.addEventListener('visibilitychange', function () {
            if (document.hidden) { stopAuto(); } else { startAuto(); }
        });

        show(active);
        startAuto();
    });

    // ── Editorial gallery ───────────────────────────────────
    document.querySelectorAll('[data-gallery-showcase]').forEach(function (gallery) {
        const images = Array.from(gallery.querySelectorAll('.mn-gallery-main'));
        const thumbs = Array.from(gallery.querySelectorAll('[data-gallery-index]'));
        const count = gallery.querySelector('[data-gallery-count]');
        const title = gallery.querySelector('[data-gallery-title]');
        const text = gallery.querySelector('[data-gallery-text]');
        const prev = gallery.querySelector('[data-gallery-prev]');
        const next = gallery.querySelector('[data-gallery-next]');
        if (!images.length || !thumbs.length) return;
        let current = 0;

        function showGalleryImage(index) {
            const active = (index + images.length) % images.length;
            current = active;
            images.forEach(function (image, i) { image.classList.toggle('active', i === active); });
            thumbs.forEach(function (thumb, i) { thumb.classList.toggle('active', i === active); });
            if (count) count.textContent = String(active + 1).padStart(2, '0') + ' / ' + String(images.length).padStart(2, '0');
            if (title) title.textContent = thumbs[active].dataset.galleryTitle || '';
            if (text) text.textContent = thumbs[active].dataset.galleryText || '';
            if (thumbs[active] && thumbs[active].scrollIntoView) {
                thumbs[active].scrollIntoView({ behavior: 'smooth', inline: 'center', block: 'nearest' });
            }
        }

        thumbs.forEach(function (thumb) {
            thumb.addEventListener('click', function () {
                showGalleryImage(+thumb.dataset.galleryIndex || 0);
            });
        });
        if (prev) prev.addEventListener('click', function () { showGalleryImage(current - 1); });
        if (next) next.addEventListener('click', function () { showGalleryImage(current + 1); });
        showGalleryImage(0);
    });

    // ── Experience image tabs ───────────────────────────────
    document.querySelectorAll('[data-experience-tabs]').forEach(function (section) {
        const tabs = Array.from(section.querySelectorAll('[data-experience-tab]'));
        const photos = Array.from(section.querySelectorAll('[data-experience-photo]'));
        const count = section.querySelector('[data-experience-count]');
        const caption = section.querySelector('[data-experience-caption]');
        if (!tabs.length || !photos.length) return;

        function showExperience(index) {
            const active = (index + tabs.length) % tabs.length;
            tabs.forEach(function (tab, i) { tab.classList.toggle('active', i === active); });
            photos.forEach(function (photo, i) { photo.classList.toggle('active', i === active); });
            if (count) count.textContent = String(active + 1).padStart(2, '0') + ' / ' + String(tabs.length).padStart(2, '0');
            if (caption) caption.textContent = tabs[active].dataset.experienceTitle || '';
        }

        tabs.forEach(function (tab) {
            tab.addEventListener('click', function () { showExperience(+tab.dataset.experienceTab || 0); });
        });
        showExperience(0);
    });

    // ── Routes terrain selector ─────────────────────────────
    document.querySelectorAll('[data-routes-tabs]').forEach(function (section) {
        const tabs = Array.from(section.querySelectorAll('[data-route-tab]'));
        const images = Array.from(section.querySelectorAll('[data-route-image]'));
        const dir = section.querySelector('[data-route-dir]');
        const name = section.querySelector('[data-route-name]');
        if (!tabs.length || !images.length) return;

        function showRoute(index) {
            const active = (index + tabs.length) % tabs.length;
            tabs.forEach(function (tab, i) { tab.classList.toggle('active', i === active); });
            images.forEach(function (image, i) { image.classList.toggle('active', i === active); });
            if (dir) dir.textContent = tabs[active].dataset.routeDir || '';
            if (name) name.textContent = tabs[active].dataset.routeName || '';
        }

        tabs.forEach(function (tab) {
            tab.addEventListener('click', function () { showRoute(+tab.dataset.routeTab || 0); });
        });
        showRoute(0);
    });

    // ============================================================
    // APPLY NOW MODAL — 4-step
    // ============================================================
    const backdrop   = document.getElementById('mn-modal-backdrop');
    const modal      = document.getElementById('mn-modal');
    const closeBtn   = document.getElementById('mn-modal-close');
    const backBtn    = document.getElementById('mn-modal-back');
    const nextBtn    = document.getElementById('mn-modal-next');
    const stepsEl    = document.getElementById('mn-modal-steps');
    const footerEl   = document.getElementById('mn-modal-footer');
    const successEl  = document.getElementById('mn-modal-success');
    const applyForm  = document.getElementById('mn-apply-form');
    const TOTAL      = 4;
    let   currentStep = 1;

    function getStepPanel(n) {
        return applyForm ? applyForm.querySelector('[data-step="' + n + '"]') : null;
    }
    function getDots() {
        return stepsEl ? stepsEl.querySelectorAll('.mn-modal-step-dot') : [];
    }

    function renderStep(n) {
        // panels
        for (let i = 1; i <= TOTAL; i++) {
            const p = getStepPanel(i);
            if (p) p.classList.toggle('active', i === n);
        }
        // dots
        getDots().forEach(function (d) {
            const s = +d.dataset.step;
            d.classList.toggle('active', s === n);
            d.classList.toggle('done',   s < n);
        });
        // buttons
        if (backBtn) backBtn.disabled = (n === 1);
        if (nextBtn) {
            if (n === TOTAL) {
                nextBtn.textContent = 'Submit';
            } else {
                nextBtn.innerHTML = 'Next &#8594;';
            }
        }
        currentStep = n;
    }

    function openModal(expedition) {
        if (!backdrop) return;
        // Pre-select expedition if passed
        if (expedition) {
            const sel = applyForm && applyForm.querySelector('[name="mn_expedition"]');
            if (sel) {
                Array.from(sel.options).forEach(function (o) {
                    if (o.value === expedition) o.selected = true;
                });
            }
        }
        renderStep(1);
        backdrop.classList.add('open');
        document.body.style.overflow = 'hidden';
        scrollEl.style.overflow = 'hidden';
        // Focus first input
        const firstInput = applyForm && applyForm.querySelector('input, select');
        if (firstInput) setTimeout(function () { firstInput.focus(); }, 50);
    }

    function closeModal() {
        if (!backdrop) return;
        backdrop.classList.remove('open');
        document.body.style.overflow = '';
        scrollEl.style.overflow = '';
    }

    function resetModal() {
        renderStep(1);
        if (successEl) successEl.classList.remove('visible');
        if (applyForm) { applyForm.style.display = ''; applyForm.reset(); }
        if (footerEl)  footerEl.style.display = '';
        if (stepsEl)   stepsEl.style.display = '';
    }

    // Open on any .mn-apply-btn click
    document.addEventListener('click', function (e) {
        const btn = e.target.closest('.mn-apply-btn');
        if (!btn) return;
        e.preventDefault();
        closeMobile();
        resetModal();
        openModal();
    });

    // Open with pre-selected expedition from card
    document.addEventListener('click', function (e) {
        const card = e.target.closest('.mn-card');
        if (!card) return;
        // Only intercept if the card href leads to /expeditions/
        const href = card.getAttribute('href') || '';
        if (!href.startsWith('/expeditions/')) return;
        // For now still navigate — don't intercept cards
    });

    if (closeBtn) closeBtn.addEventListener('click', closeModal);
    if (backdrop) {
        backdrop.addEventListener('click', function (e) {
            if (e.target === backdrop) closeModal();
        });
    }
    document.addEventListener('keydown', function (e) {
        if (e.key === 'Escape' && backdrop && backdrop.classList.contains('open')) closeModal();
    });

    // Next / Back
    if (nextBtn) {
        nextBtn.addEventListener('click', function () {
            if (currentStep < TOTAL) {
                renderStep(currentStep + 1);
            } else {
                submitApplyForm();
            }
        });
    }
    if (backBtn) {
        backBtn.addEventListener('click', function () {
            if (currentStep > 1) renderStep(currentStep - 1);
        });
    }

    // ── Submit form via fetch ────────────────────────────────
    function submitApplyForm() {
        if (!applyForm) return;

        // Basic validation step 4
        const agree = applyForm.querySelector('[name="mn_agree"]');
        if (agree && !agree.checked) {
            agree.focus();
            return;
        }

        const data = new FormData(applyForm);
        // Build a plain object for display / email
        const payload = {};
        data.forEach(function (v, k) { payload[k] = v; });

        // Disable submit while sending
        if (nextBtn) { nextBtn.disabled = true; nextBtn.textContent = '…'; }

        // Try the Minuru application endpoint first, then fall back to Odoo contactus.
        const csrfInput = applyForm.querySelector('input[name="csrf_token"]') || document.querySelector('input[name="csrf_token"]');
        const csrf = csrfInput ? csrfInput.value : '';

        const applicationBody = new URLSearchParams();
        applicationBody.append('csrf_token', csrf);
        Object.keys(payload).forEach(function (key) {
            applicationBody.append(key, payload[key] || '');
        });

        const contactBody = new URLSearchParams();
        contactBody.append('csrf_token',  csrf);
        contactBody.append('contact_name', payload.mn_name   || '');
        contactBody.append('email_from',   payload.mn_email  || '');
        contactBody.append('phone',        payload.mn_whatsapp || '');
        contactBody.append('subject',      'Apply Now: ' + (payload.mn_expedition || 'Expedition'));
        contactBody.append('description',
            'Country: '   + (payload.mn_country  || '') + '\n' +
            'Age: '       + (payload.mn_age      || '') + '\n' +
            'Group: '     + (payload.mn_groupsize || '') + '\n' +
            'Expedition: '+ (payload.mn_expedition|| '') + '\n' +
            'Month: '     + (payload.mn_month    || '') + '\n' +
            'VIP: '       + (payload.mn_vip      || '') + '\n' +
            'Off-road exp: '+ (payload.mn_exp    || '') + '\n' +
            'Driving: '   + (payload.mn_driving  || '') + '\n' +
            'Fitness: '   + (payload.mn_fitness  || '') + '\n' +
            'Expectations: '+ (payload.mn_expect || '') + '\n' +
            'Special: '   + (payload.mn_special  || '')
        );

        function postForm(url, formBody) {
            return fetch(url, {
                method: 'POST',
                headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
                body: formBody.toString(),
            }).then(function (response) {
                if (!response.ok) throw new Error('Request failed');
                return response;
            });
        }

        postForm('/minuru/apply', applicationBody)
        .then(function () { showSuccess(); })
        .catch(function () {
            return postForm('/contactus', contactBody).then(function () { showSuccess(); });
        })
        .catch(function () {
            if (nextBtn) { nextBtn.disabled = false; nextBtn.textContent = 'Submit'; }
        });
    }

    function showSuccess() {
        if (applyForm)  applyForm.style.display = 'none';
        if (footerEl)   footerEl.style.display  = 'none';
        if (stepsEl)    stepsEl.style.display    = 'none';
        if (successEl)  successEl.classList.add('visible');
        if (nextBtn)    { nextBtn.disabled = false; nextBtn.textContent = 'Submit'; }
    }

})();
