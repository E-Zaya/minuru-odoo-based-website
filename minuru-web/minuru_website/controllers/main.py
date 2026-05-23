# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

# ── Expedition data ──────────────────────────────────────────────────────────
# Each entry maps slug → template variables consumed by expedition_detail.
EXPEDITIONS = {
    'gobi': {
        'exp_slug':        'gobi',
        'exp_title_en':    'Gobi Desert',
        'exp_title_mn':    'Говь Цөл',
        'exp_type_en':     'Desert & Dunes',
        'exp_type_mn':     'Цөл & Элсэн манхан',
        'exp_duration_en': '10 Days',
        'exp_duration_mn': '10 хоног',
        'exp_level_en':    'Moderate',
        'exp_level_mn':    'Дунд зэрэг',
        'exp_tagline_en':  'Silence, sand, and the infinite sky of the world\'s greatest cold desert.',
        'exp_tagline_mn':  'Дэлхийн хамгийн том хүйтэн цөлийн чимээгүй байдал, элс, хязгааргүй тэнгэр.',
        'exp_description_en': (
            'The Gobi is not just a desert — it is a living landscape of contrasts. '
            'Towering sand dunes meet ancient canyons, saxaul forests, and the bones of dinosaurs. '
            'We drive deep into the heart of this extraordinary terrain, camping under skies '
            'untouched by light pollution, guided by local nomad families who have read this '
            'land for generations.'
        ),
        'exp_description_mn': (
            'Говь бол зөвхөн цөл биш — энэ бол эсрэгцэлийн амьд ертөнц. '
            'Өндөр элсэн манхан нь эртний хавцал, саксаулын ой, '
            'динозаврын яснуудтай нийлдэг. '
            'Бид энэ гайхалтай газар нутгийн зүрхэнд гүнзгий орж, '
            'гэрэл бохирдолгүй тэнгэрийн доор хуаранддаг.'
        ),
        'exp_price':       '3,200',
        'exp_hero_img':    '/minuru_website/static/src/img/gobi_01.png',
        'exp_img_1':       '/minuru_website/static/src/img/mongolia_image_02.png',
        'exp_img_2':       '/minuru_website/static/src/img/mongolia_image_03.png',
        'exp_img_3':       '/minuru_website/static/src/img/mongolia_image_04.png',
        'exp_highlights_en': [
            'Khongoryn Els — the Singing Dunes, rising 300 m above the plain',
            'Yolyn Am ice canyon, even in midsummer',
            'Bayanzag — the Flaming Cliffs, treasure trove of dinosaur fossils',
            'Overnight in traditional ger camps with nomad families',
            'Stargazing in total darkness, zero light pollution',
        ],
        'exp_highlights_mn': [
            'Хонгорын Элс — 300 м өндөрт хүрэх Дуулах Элсэн манхан',
            'Ёлын Ам — зуны дунд ч мөс хайлахгүй хавцал',
            'Баянзаг — Дөлөн хад, динозаврын олдворын баялаг',
            'Нүүдэлчин гэр бүлтэй уламжлалт гэрт шөнийн дугуйлан',
            'Гэрэл бохирдолгүй орчинд одод ажиглах',
        ],
    },

    'altai': {
        'exp_slug':        'altai',
        'exp_title_en':    'Altai Mountains',
        'exp_title_mn':    'Алтайн Нуруу',
        'exp_type_en':     'Mountain & Eagle Culture',
        'exp_type_mn':     'Уул & Бүргэд соёл',
        'exp_duration_en': '12 Days',
        'exp_duration_mn': '12 хоног',
        'exp_level_en':    'Challenging',
        'exp_level_mn':    'Хүнд',
        'exp_tagline_en':  'Ancient eagle hunters, jagged peaks, and the last true wilderness of Central Asia.',
        'exp_tagline_mn':  'Эртний бүргэдчид, цоорхой оргилууд, Төв Азийн хамгийн сүүлийн цөм.',
        'exp_description_en': (
            'The Mongolian Altai is the homeland of the Kazakh eagle hunters, '
            'a culture stretching back over four millennia. Remote, dramatic, and '
            'profoundly beautiful, this region demands a spirit of adventure. '
            'We traverse high passes, camp beside glacial rivers, and share evenings '
            'with eagle hunter families in their winter homes.'
        ),
        'exp_description_mn': (
            'Монголын Алтай бол Казах бүргэдчдийн эх нутаг, '
            'дөрвөн мянган жилийн түүхтэй соёл. '
            'Алслагдсан, гайхалтай, гүн гүнзгий үзэсгэлэнтэй энэ бүс нутаг '
            'адал явдлын сэтгэлийг шаарддаг.'
        ),
        'exp_price':       '3,800',
        'exp_hero_img':    '/minuru_website/static/src/img/mongolia_image_02.png',
        'exp_img_1':       '/minuru_website/static/src/img/mongolia_image_03.png',
        'exp_img_2':       '/minuru_website/static/src/img/mongolia_image_04.png',
        'exp_img_3':       '/minuru_website/static/src/img/mongolia_image_05.png',
        'exp_highlights_en': [
            'Witness a live eagle hunting demonstration with a master Kazakh eagle hunter',
            'Traverse the 3,000 m Tsast Uul ("Snow Mountain") pass',
            'Visit the ancient Turkic stone men (balbal) scattered across the steppe',
            'Kayak on the pristine Khovd River headwaters',
            'Camp beneath the Altai\'s star-filled skies at 2,200 m elevation',
        ],
        'exp_highlights_mn': [
            'Казах бүргэдчинтэй амьд бүргэд агнуурын үзүүлбэр',
            '3,000 м Цаст Уулын давааг туулах',
            'Тал нутагт тарсан эртний Түрэгийн чулуун баримал (балбал) үзэх',
            'Ховд голын эхэнд каяк унах',
            '2,200 м өндөрт Алтайн одоор дүүрэн тэнгэрийн доор хуарандах',
        ],
    },

    'khuvsgul': {
        'exp_slug':        'khuvsgul',
        'exp_title_en':    'Khuvsgul Lake',
        'exp_title_mn':    'Хөвсгөл Нуур',
        'exp_type_en':     'Lake & Reindeer Herders',
        'exp_type_mn':     'Нуур & Цаа буга малчид',
        'exp_duration_en': '9 Days',
        'exp_duration_mn': '9 хоног',
        'exp_level_en':    'Moderate',
        'exp_level_mn':    'Дунд зэрэг',
        'exp_tagline_en':  'The "Blue Pearl of Mongolia" and the last reindeer-herding Tsaatan people.',
        'exp_tagline_mn':  '"Монголын цэнхэр сувд" ба сүүлийн Цаатан цаа буга малчид.',
        'exp_description_en': (
            'Lake Khuvsgul holds nearly 70% of Mongolia\'s fresh water and borders the Siberian taiga. '
            'This expedition combines the ethereal beauty of the lake with a rare visit to the Tsaatan — '
            'reindeer herders whose culture is found nowhere else on earth. '
            'We journey by horse through deep forest to reach their remote camps.'
        ),
        'exp_description_mn': (
            'Хөвсгөл нуур Монголын цэвэр усны бараг 70%-ийг агуулж, '
            'Сибирийн тайгатай хиллэдэг. '
            'Энэхүү экспедиц нуурын гоо үзэсгэлэнтэй Цаатан буюу '
            'цаа буга малчдад зочлохыг хослуулдаг.'
        ),
        'exp_price':       '2,900',
        'exp_hero_img':    '/minuru_website/static/src/img/mongolia_image_03.png',
        'exp_img_1':       '/minuru_website/static/src/img/mongolia_image_04.png',
        'exp_img_2':       '/minuru_website/static/src/img/mongolia_image_05.png',
        'exp_img_3':       '/minuru_website/static/src/img/mongolia_image_06.png',
        'exp_highlights_en': [
            'Paddleboard or kayak on Mongolia\'s most sacred lake',
            'Horseback journey through old-growth taiga forest to Tsaatan camps',
            'Stay with a reindeer-herding family and learn their ancient practices',
            'Spot rare wildlife: Siberian ibex, argali sheep, and migratory birds',
            'Swim or bathe in pristine glacial springs',
        ],
        'exp_highlights_mn': [
            'Монголын хамгийн ариун нуурт дэвсгэр самбар эсвэл каяк унах',
            'Цаатаны хуаран руу морьдоор эртний тайгын ойгоор аялах',
            'Цаа буга малчин гэр бүлд зочлож тэдний эртний уламжлалыг сурах',
            'Ховор амьтад: Сибирийн ямаа, аргаль хонь, нүүдлийн шувуу',
            'Цэвэр мөсний булагт усанд орох',
        ],
    },

    'central': {
        'exp_slug':        'central',
        'exp_title_en':    'Central Mongolia',
        'exp_title_mn':    'Төв Монгол',
        'exp_type_en':     'Heartland & History',
        'exp_type_mn':     'Голомт & Түүх',
        'exp_duration_en': '8 Days',
        'exp_duration_mn': '8 хоног',
        'exp_level_en':    'Easy–Moderate',
        'exp_level_mn':    'Хялбар–Дунд',
        'exp_tagline_en':  'The spiritual and historical heartland of the Mongol Empire.',
        'exp_tagline_mn':  'Монголын эзэнт гүрний оюун санааны болон түүхийн голомт.',
        'exp_description_en': (
            'Central Mongolia is where the story of the Mongol Empire was written. '
            'From the ancient capital of Karakorum to the sacred mountain of Khangai, '
            'this route reveals a land shaped by both conquest and deep spirituality. '
            'Rolling grasslands, ancient monasteries, and warm nomadic hospitality define every day.'
        ),
        'exp_description_mn': (
            'Төв Монгол бол Монголын эзэнт гүрний түүх бичигдсэн газар. '
            'Эртний нийслэл Хархорумаас Хангайн ариун уул хүртэл '
            'энэхүү маршрут байлдан дагуулал болон гүн шашин шүтлэгийн '
            'хоёроор хэлбэрлэгдсэн газар нутгийг илчилдэг.'
        ),
        'exp_price':       '2,400',
        'exp_hero_img':    '/minuru_website/static/src/img/mongolia_image_04.png',
        'exp_img_1':       '/minuru_website/static/src/img/mongolia_image_05.png',
        'exp_img_2':       '/minuru_website/static/src/img/mongolia_image_06.png',
        'exp_img_3':       '/minuru_website/static/src/img/mongolia_image_07.png',
        'exp_highlights_en': [
            'Karakorum — the ruins of Genghis Khan\'s capital city',
            'Erdene Zuu Monastery, the first Buddhist monastery in Mongolia (1586)',
            'Orkhon Valley — UNESCO World Heritage landscape',
            'Horseback riding across the open steppe with nomad guides',
            'Overnight in luxury ger camps with traditional meals',
        ],
        'exp_highlights_mn': [
            'Хархорум — Чингис хааны нийслэл хотын туурь',
            'Эрдэнэ Зуу хийд — Монголын анхны Буддын хийд (1586)',
            'Орхоны хөндий — ЮНЕСКО-гийн дэлхийн өвийн газар',
            'Нүүдэлчин гидтай нээлттэй тал нутгаар морь унах',
            'Уламжлалт хоолтой тансаг гэрийн буудалд шөнийн дугуйлан',
        ],
    },

    'eastern-steppe': {
        'exp_slug':        'eastern-steppe',
        'exp_title_en':    'Eastern Steppe',
        'exp_title_mn':    'Зүүн Тал Нутаг',
        'exp_type_en':     'Wilderness & Wildlife',
        'exp_type_mn':     'Зэрлэг байгаль & Амьтад',
        'exp_duration_en': '11 Days',
        'exp_duration_mn': '11 хоног',
        'exp_level_en':    'Moderate',
        'exp_level_mn':    'Дунд зэрэг',
        'exp_tagline_en':  'The last great migration on earth — a million gazelle across the endless plain.',
        'exp_tagline_mn':  'Дэлхийн хамгийн сүүлийн агуу нүүдэл — хязгааргүй талаар нэг сая зурам.',
        'exp_description_en': (
            'The Eastern Steppe is one of the last intact grassland ecosystems on Earth. '
            'Here, vast herds of Mongolian gazelle still undertake their ancient migration, '
            'and the horizon stretches unbroken for hundreds of kilometers. '
            'This is raw, primal Mongolia — no fences, no roads, no noise but wind and hooves.'
        ),
        'exp_description_mn': (
            'Зүүн тал нутаг бол дэлхийд үлдсэн хамгийн сүүлийн бүрэн нутаг дэвсгэрийн '
            'нэг юм. Энд Монголын зурамны асар том сүрэг одоо ч эртний нүүдлээ хийж, '
            'хэдэн зуун километр тэнгэр газрын зааг тасрахгүй сунадаг.'
        ),
        'exp_price':       '3,100',
        'exp_hero_img':    '/minuru_website/static/src/img/mongolia_image_05.png',
        'exp_img_1':       '/minuru_website/static/src/img/mongolia_image_06.png',
        'exp_img_2':       '/minuru_website/static/src/img/mongolia_image_07.png',
        'exp_img_3':       '/minuru_website/static/src/img/mongolia_image_08.png',
        'exp_highlights_en': [
            'Witness the Mongolian gazelle migration — up to one million animals',
            'Spot white-tailed eagle, steppe eagle, and demoiselle crane',
            'Visit the Dadal region, birthplace of Genghis Khan',
            'Buir Lake — vast shallow lake rich with migratory waterfowl',
            'Endless off-road driving across pristine virgin steppe',
        ],
        'exp_highlights_mn': [
            'Монголын зурамны нүүдлийг ажиглах — нэг сая хүртэл амьтан',
            'Цагаан сүүлт бүргэд, тал нутгийн бүргэд, хонхорхой дэгдээхэй',
            'Чингис хааны төрсөн нутаг Дадал руу зочлох',
            'Буйр нуур — нүүдлийн усны шувуугаар баялаг том нуур',
            'Хязгааргүй хүрэлцэх замгүй талаар жолоодох',
        ],
    },

    'gobi-altai': {
        'exp_slug':        'gobi-altai',
        'exp_title_en':    'Gobi Altai',
        'exp_title_mn':    'Говийн Алтай',
        'exp_type_en':     'Desert Mountain Fusion',
        'exp_type_mn':     'Цөл ба уулын нэгдэл',
        'exp_duration_en': '13 Days',
        'exp_duration_mn': '13 хоног',
        'exp_level_en':    'Challenging',
        'exp_level_mn':    'Хүнд',
        'exp_tagline_en':  'Where desert meets the mountains — two of Mongolia\'s most dramatic landscapes as one.',
        'exp_tagline_mn':  'Цөл уультай уулзах газар — Монголын хамгийн гайхалтай хоёр газар нэгэн дор.',
        'exp_description_en': (
            'The Gobi Altai combines the raw drama of the Gobi Desert with the towering '
            'mountain ranges that rise unexpectedly from the sand. This is Mongolia\'s '
            'most geologically diverse landscape — ancient sea beds, volcanic craters, '
            'ice-capped peaks, and sand seas all within a single expedition.'
        ),
        'exp_description_mn': (
            'Говийн Алтай нь Говь цөлийн хатуу жүжиг болон элснээс гэнэтийн '
            'өндрөөр өргөгдсөн уулсыг хослуулдаг. '
            'Энэ бол Монголын геологийн хувьд хамгийн олон янзын газар нутаг — '
            'эртний далайн ёроол, галт уулын тогоо, мөст оргилууд, элсэн далай.'
        ),
        'exp_price':       '4,100',
        'exp_hero_img':    '/minuru_website/static/src/img/mongolia_image_06.png',
        'exp_img_1':       '/minuru_website/static/src/img/mongolia_image_07.png',
        'exp_img_2':       '/minuru_website/static/src/img/mongolia_image_08.png',
        'exp_img_3':       '/minuru_website/static/src/img/mongolia_image_09.png',
        'exp_highlights_en': [
            'Eej Khad — the sacred "Mother Rock" revered by Mongolians',
            'Ikh Bogd massif — highest peak in the Gobi Altai range at 3,957 m',
            'Biger lake oasis surrounded by desert',
            'Petroglyphs dating back 8,000 years in remote canyons',
            'Combined ger and wild camping across two distinct ecosystems',
        ],
        'exp_highlights_mn': [
            'Эж Хад — Монголчуудын хүндэтгэдэг ариун "Эх Чулуу"',
            'Их Богд массив — Говийн Алтайн хамгийн өндөр оргил 3,957 м',
            'Цөлөөр хүрэгдсэн Бигэрийн нуурын оазис',
            'Алслагдсан хавцлын 8,000 жилийн өмнөх хадны зураг',
            'Хоёр өөр экосистемд гэр болон зэрлэг хуаран хослуулах',
        ],
    },

    'western': {
        'exp_slug':        'western',
        'exp_title_en':    'Western Mongolia',
        'exp_title_mn':    'Баруун Монгол',
        'exp_type_en':     'Multi-Ethnic Explorer',
        'exp_type_mn':     'Олон үндэстний судлаач',
        'exp_duration_en': '14 Days',
        'exp_duration_mn': '14 хоног',
        'exp_level_en':    'Challenging',
        'exp_level_mn':    'Хүнд',
        'exp_tagline_en':  'Five ethnicities, four mountain ranges, and the most remote terrain in Mongolia.',
        'exp_tagline_mn':  'Таван үндэстэн, дөрвөн нурууны хэлхээ, Монголын хамгийн алслагдсан нутаг.',
        'exp_description_en': (
            'Western Mongolia is home to Kazakh, Tuvan, Khoton, Uriankhai, and Mongolian '
            'communities — each with distinct traditions, music, and crafts. '
            'This is our most ambitious expedition, crossing high alpine passes, '
            'remote river valleys, and vast wilderness areas that see fewer than '
            'a hundred foreign visitors per year.'
        ),
        'exp_description_mn': (
            'Баруун Монголд Казах, Тувин, Хотон, Урианхай, Монгол '
            'олон нийтүүд амьдарч — тус бүр өөрийн уламжлал, хөгжим, урлагтай. '
            'Энэ бол бидний хамгийн их хүсэл эрмэлзлэлтэй экспедиц бөгөөд '
            'жилд зуу хүрэхгүй гадаадын зочин очдог газар нутгаар дамжина.'
        ),
        'exp_price':       '4,600',
        'exp_hero_img':    '/minuru_website/static/src/img/mongolia_image_07.png',
        'exp_img_1':       '/minuru_website/static/src/img/mongolia_image_08.png',
        'exp_img_2':       '/minuru_website/static/src/img/mongolia_image_09.png',
        'exp_img_3':       '/minuru_website/static/src/img/mongolia_image_10.png',
        'exp_highlights_en': [
            'Tavan Bogd — "Five Saints" massif, summit of Mongolia at 4,374 m',
            'Potanin Glacier — one of the largest glaciers in Central Asia',
            'Tolbo Lake — high altitude lake at 2,080 m, mirroring the Altai',
            'Tsagaan Gol petroglyphs — the world\'s largest concentration of ibex carvings',
            'Kazakh Golden Eagle Festival cultural immersion',
        ],
        'exp_highlights_mn': [
            'Таван Богд — "Таван бурхан" массив, Монголын дээд цэг 4,374 м',
            'Потаниний мөсөн гол — Төв Азийн хамгийн том мөсөн голуудын нэг',
            'Цагаан нуур — 2,080 м өндөрт Алтайг тусгасан нуур',
            'Цагаан голын хадны зураг — дэлхийн хамгийн том ямааны сийлбэрийн цуглуулга',
            'Казахын алтан бүргэдний наадмын соёлд дүрэгдэх',
        ],
    },

    'northern': {
        'exp_slug':        'northern',
        'exp_title_en':    'Northern Forest Belt',
        'exp_title_mn':    'Хойт Ойн Бүс',
        'exp_type_en':     'Taiga & Rivers',
        'exp_type_mn':     'Тайга & Голууд',
        'exp_duration_en': '10 Days',
        'exp_duration_mn': '10 хоног',
        'exp_level_en':    'Moderate',
        'exp_level_mn':    'Дунд зэрэг',
        'exp_tagline_en':  'Mongolia\'s secret green world — dense taiga, wild rivers, and bear country.',
        'exp_tagline_mn':  'Монголын нууц ногоон ертөнц — нягт тайга, зэрлэг голууд, баавгайн нутаг.',
        'exp_description_en': (
            'Most visitors never discover that northern Mongolia is covered by a dense, '
            'untouched Siberian taiga. This region — a transition zone between steppe and '
            'boreal forest — is home to brown bear, wolverine, lynx, and reindeer. '
            'We explore by off-road vehicle and on foot, camping beside rivers '
            'still rich with taimen, the world\'s largest trout.'
        ),
        'exp_description_mn': (
            'Ихэнх зочид Монголын умардад нягт, хүрэлцэх хорин байгалийн '
            'Сибирийн тайга байдгийг хэзээ ч мэдэхгүй. '
            'Тал нутаг ба шилмүүст ойн дунд шилжилтийн бүс болох энэ нутаг '
            'бор баавгай, арслангийн, хысаа, цаа буга нутаглах газар юм.'
        ),
        'exp_price':       '2,800',
        'exp_hero_img':    '/minuru_website/static/src/img/mongolia_image_08.png',
        'exp_img_1':       '/minuru_website/static/src/img/mongolia_image_09.png',
        'exp_img_2':       '/minuru_website/static/src/img/mongolia_image_10.png',
        'exp_img_3':       '/minuru_website/static/src/img/mongolia_image_11.png',
        'exp_highlights_en': [
            'Fly-fishing for taimen — the world\'s largest salmonid, up to 1.5 m long',
            'Track brown bear through old-growth forest with expert naturalist guides',
            'Selenge River source — headwaters flowing to Lake Baikal',
            'Remote forest monasteries accessible only by 4WD',
            'Dawn wildlife watches from elevated hides',
        ],
        'exp_highlights_mn': [
            'Тайменд хийсэх загас агнуур — дэлхийн хамгийн том лосос хүртэл 1.5 м урт',
            'Мэргэжлийн байгаль судлаачтай хамт бор баавгайн ул мөрийг мөшгөх',
            'Сэлэнгэ мөрний эх — Байгал нуур руу урсдаг гарлаа',
            'Зөвхөн 4 дугуйт машинаар хүрч болох алслагдсан ойн хийдүүд',
            'Өглөөний амьтад ажиглах',
        ],
    },

    'steppe-lake': {
        'exp_slug':        'steppe-lake',
        'exp_title_en':    'Steppe & Lakes',
        'exp_title_mn':    'Тал & Нуур',
        'exp_type_en':     'Nomadic Immersion',
        'exp_type_mn':     'Нүүдэлчдийн дотор',
        'exp_duration_en': '7 Days',
        'exp_duration_mn': '7 хоног',
        'exp_level_en':    'Easy',
        'exp_level_mn':    'Хялбар',
        'exp_tagline_en':  'The essential Mongolia — horseback riding, nomad families, and mirror-calm lakes.',
        'exp_tagline_mn':  'Монголын мөн чанар — морь унах, нүүдэлчин гэр бүл, толь шиг тайван нуурууд.',
        'exp_description_en': (
            'If you have one week and want the soul of Mongolia, this is the journey. '
            'The Steppe & Lakes expedition is our most accessible route, designed for '
            'first-time visitors who want authentic nomadic immersion without extreme terrain. '
            'We stay with nomad families, ride horses across open steppe, and watch the '
            'seasons move across one of the world\'s most peaceful landscapes.'
        ),
        'exp_description_mn': (
            'Хэрэв танд нэг долоо хоног байгаа бол Монголын сүнсийг мэдрэхийг хүсч байвал '
            'энэ бол таны аялал. '
            'Тал & Нуурын экспедиц нь туйлын газар нутаггүйгээр жинхэнэ '
            'нүүдэлчдийн орчинд дүрэгдэхийг хүссэн анхны зочдод зориулагдсан.'
        ),
        'exp_price':       '1,900',
        'exp_hero_img':    '/minuru_website/static/src/img/mongolia_image_09.png',
        'exp_img_1':       '/minuru_website/static/src/img/mongolia_image_10.png',
        'exp_img_2':       '/minuru_website/static/src/img/mongolia_image_11.png',
        'exp_img_3':       '/minuru_website/static/src/img/hero.png',
        'exp_highlights_en': [
            'Terkhiin Tsagaan Nuur (White Lake) — extinct volcanic crater filled with crystal water',
            'Horseback riding with nomad herder family across open grassland',
            'Traditional Mongolian wrestling (bokh) and archery demonstrations',
            'Sunset over Ogii Lake with thousands of migratory waterfowl',
            'Naadam-style cultural evening with music, dance, and food',
        ],
        'exp_highlights_mn': [
            'Тэрхийн Цагаан нуур — кристал усаар дүүрсэн идэвхгүй галт уулын тогоо',
            'Нүүдэлчин малчин гэр бүлтэй нээлттэй нугаар морь унах',
            'Уламжлалт Монгол бөх, харваа, морин хуур үзүүлбэр',
            'Нүүдлийн усны шувуудтай Огийн нуурт нарны жаргалт',
            'Хөгжим, бүжиг, хоолтой Наадамын соёлын орой',
        ],
    },
}


class MinuruWebsite(http.Controller):

    @http.route('/expeditions/<string:slug>', auth='public', website=True, sitemap=True)
    def expedition_detail(self, slug, **kwargs):
        data = EXPEDITIONS.get(slug)
        if not data:
            return request.not_found()
        return request.render('minuru_website.expedition_detail', data)

    @http.route('/expeditions', auth='public', website=True, sitemap=True)
    def expeditions_index(self, **kwargs):
        # Redirect to home expeditions section
        return request.redirect('/#expeditions')
