# खोज रिकॉर्ड और संग्रह-निर्णय

2026-11-05 को प्रारंभिक संस्करण पूर्ण: 41 प्रोजेक्ट, 6 श्रेणियाँ, 13 डी-डुप्लिकेट संदर्भ प्रोजेक्टों की पूरी कवरेज। 2026-11-06 में उपयोगकर्ता के पूरक इनपुट के आधार पर Reveric जोड़ा; वर्तमान में 42 प्रोजेक्ट, 14 संदर्भ प्रोजेक्ट। इस दौर का फ़ोकस प्रोजेक्ट और इंप्लीमेंटेशन पर था, संबंधित शोध-पत्रों को अलग पत्र-सूची में नहीं बढ़ाया गया।

## संदर्भ प्रोजेक्टों से निकाले गए खोज-अक्ष

| दिशा | अंग्रेज़ी कीवर्ड | चीनी कीवर्ड |
| --- | --- | --- |
| पूर्ण लेखन टूल | AI novel writer, writing workspace, fiction IDE, local-first | AI 小说写作、小说工作台、桌面码字软件 |
| दीर्घ-कृति ऑटोमेशन | long-form fiction, writing agent, novel generator, harness | 长篇生成、分章写作、写作 Agent |
| स्थिति और निरंतरता | story bible, character state, foreshadowing, continuity, RAG | 世界观、人物状态、伏笔、连贯性、长期记忆 |
| Agent संसाधन | novel writing skill, workflow, prompt framework | 小说 Skill、网文技能、方法框架 |
| संशोधन | narrative revision, humanizer, style lint, editing | 叙事修复、去模板化、文风、审稿 |
| रूपांतरण | screenplay, short drama, story adaptation, narration | 剧本、短剧、小说改编、影视解说 |

## तीन दौर की खोज

| दौर | बैच | रिज़ल्ट | नए स्रोत | नए स्रोत दर |
| --- | --- | --- | --- | --- |
| 1 | 15 | 331 | 300 | 90.6% |
| 2 | 4 | 127 | 90 | 70.9% |
| 3 | 3 | 17 | 15 | 88.2% |

कुल 22 खोज या सत्यापन बैच, जिनमें वेब खोज, GitHub native search, क्यूरेटेड डायरेक्टरी के लिंक-संग्रह, और रिपॉज़िटरी व मीट्रिक के बैच-सत्यापन शामिल। स्रोत-संख्या खोज-ledger के URL की गिनती है; यह संग्रहीत प्रोजेक्टों की संख्या नहीं है और हर candidate प्रासंगिक भी नहीं था।

पहले दौर की शुरुआत सभी संदर्भ प्रोजेक्टों से, आठ दिशाओं में: परिभाषा, मूल स्रोत, क्यूरेटेड डायरेक्टरी, रिपॉज़िटरी, तुलना, मूल्यांकन, सीमाएँ और हाल के बदलाव। GitHub पर `小说` खोजने पर reader, downloader, CMS और बुकलिस्ट मिलते हैं, जिन्हें लेखन-लक्ष्य के अनुसार हटाया गया; `easy-writing` में समान-नाम वाले development framework भी आते हैं, इसलिए केवल खोज-रैंक से संग्रह नहीं किया गया।

दूसरे दौर में Oh Story, webnovel-writer, NovelClaw, OpenFic जैसी दिशाएँ जोड़ी गईं; आधिकारिक README पढ़कर ऐप, स्किल और मेथडोलॉजी के अंतर पहचाने गए। क्यूरेटेड डायरेक्टरी सिर्फ़ सुराग के लिए उपयोग; उनका star, conference जानकारी या प्रभाव-निष्कर्ष सीधे copy नहीं किया गया।

तीसरे दौर में पुनर्नाम, license exception, उपयोगकर्ता-प्रदत्त Sepia का चीनी README सत्यापित किया और Long-Novel-GPT जोड़ा गया। सभी अंतिम प्रोजेक्टों के मीट्रिक GitHub GraphQL से एक साथ लिए गए; फ़ंक्शन-स्रोत का commit फ़िक्स किया गया।

रोकने का कारण पहले से तय तीन-दौर की सीमा थी, यह नहीं कि खोज-क्षेत्र समाप्त हो चुका है। तीसरे दौर में भी नई खोजें हुईं। vertical शैलियाँ, interactive fiction, अनुवाद, लोकल लेखन-मॉडल और पूरे industry के शॉर्ट-ड्रामा टूल अभी पूरी तरह कवर नहीं। pure उपन्यास-पठन, scraping या publishing टूल को लेखन-उपकरण के रूप में ज़बरदस्ती सूची में नहीं भरा गया।

## संदर्भ प्रोजेक्ट, नाम और डी-डुप्लिकेशन

| उपयोगकर्ता-नाम / पुराना नाम | वर्तमान संग्रह |
| --- | --- |
| Denova | [alfredxw/denova](https://github.com/alfredxw/denova) |
| 易创 easy-writing | [yilujian/easy-writing](https://github.com/yilujian/easy-writing) |
| ai-juben | [VanGong1999/juben](https://github.com/VanGong1999/juben), उपयोगकर्ता की पुष्टि पर |
| AI Novel Writer | [Pagekin](https://github.com/EthanYoQ/Pagekin), रिपॉज़िटरी का नाम बदला जा चुका; पुराना पता अपने आप redirect करता है |
| AI Novel Writing Assistant | [Biz Novel Studio](https://github.com/ExplosiveCoderflome/AI-Novel-Writing-Assistant), उसी रिपॉज़िटरी में |
| Storyteller | [Dankular/Storyteller](https://github.com/Dankular/Storyteller), README में वर्तमान नाम novel-harness |
| डुप्लिकेट Sepia और `-g` | एक ही रिपॉज़िटरी, एक ही प्रविष्टि; Skill इंस्टॉल नहीं किया गया |

सभी seed mapping [seed-references.json](../../../data/seed-references.json) में सुरक्षित हैं। canonical repo प्रोजेक्ट-डी-डुप्लिकेशन की key है; रिपॉज़िटरी पुनर्नाम से नई प्रविष्टि नहीं बनती। OpenCode पोर्ट को होस्ट और फ़ंक्शन-अंतर के कारण अलग रखा और upstream से संबंध दर्ज किया; बिना-स्पष्ट-अंतर के same-content fork संग्रह में नहीं।

## मूल दस्तावेज़ के सुधार

- [qifeng-writing](https://github.com/Yuriloll/qifeng-writing) स्पष्ट रूप से चीनी-भाषी पोस्ट और लेख केंद्रित है; शुद्ध उपन्यास के लिए अलग मेथड चाहिए, इसलिए इसे संलग्न संशोधन-उपकरण में रखा।
- [Narrator AI CLI Skill](https://github.com/NarratorAI-Studio/narrator-ai-cli-skill) फ़िल्मी व्याख्या CLI के invocation का निर्देश है; इसे मूल दीर्घ-उपन्यास जनरेटर नहीं लिखा।
- [NeuroBook](https://github.com/notnotype/neuro-book) का वर्तमान v2 पुनर्निर्माणाधीन; कुछ AI स्टूडियो क्षमताएँ roadmap पर सूचीबद्ध। डायरेक्टरी में preview-अवस्था की सीमा रखी गई।
- [Novel Studio](https://github.com/bbaz123/novel-studio) की डिफ़ॉल्ट ब्रांच experimental line है; मीट्रिक वास्तव में इसी ब्रांच से लिए गए, पुरानी main को ज़बरदस्ती नहीं अपनाया।
- [Long-Novel-GPT](https://github.com/MaoXiaoYuZ/Long-Novel-GPT) की कुछ वन-क्लिक-बुक क्षमताएँ अब भी plan में; homepage के slogan को पूर्ण-स्वीकृति नहीं माना।
- [Reveric](https://github.com/looplj/reveric) की वर्तमान डिफ़ॉल्ट ब्रांच `unstable` है; डायरेक्टरी उसी ब्रांच पर सत्यापित। इसके `NOTICES` AGPLv3 धारा 7 के तहत संशोधनों में परियोजना-एट्रिब्यूशन और मूल लिंक रखना माँगते हैं, और वाणिज्यिक लाइसेंस का पथ भी देते हैं।

## लाइसेंस सत्यापन

GitHub SPDX पहचान और मैन्युअल exception-जाँच अलग सहेजी जाती हैं। Biz Novel Studio का LICENSE AGPL और सर्विस-आधारित वाणिज्यिक अनुमोदन-नोट दोनों रखता है; Kimi Writer का LICENSE अतिरिक्त वाणिज्यिक attribution शर्त वाला पाठ है। दोनों में मूल लिंक रखे, इन्हें साधारण AGPL/MIT में सरल नहीं किया।

Agnes ने स्पष्ट कहा कि लाइसेंस घोषित नहीं है; कई छोटे लेखन Harness, Skill और evaluation रिपॉज़िटरी में संपूर्ण LICENSE नहीं मिला। README का badge या एक लाइन का MIT-दावा इन्हें स्वतः "सत्यापित" नहीं बनाता। विशिष्ट स्थिति [प्रोजेक्ट विवरण तालिका](projects.md) में। यह डायरेक्टरी लेखक-शर्तें दर्ज करती है, cross-project वाणिज्यिक-उपयोग की गारंटी नहीं देती।

## कंटेंट फैक्ट्री

`content-factory-search-api` का पालन; curl से structured search, date range **2026-08-05 से 2026-11-05**, queries `小说` और `inkos OR sepia OR 小说写作`। दोनों ने सफल JSON लौटाया पर result array खाली। full-history search नहीं चलाया; खाली नतीजे का अर्थ यह प्रोजेक्टों का अस्तित्व न होना नहीं निकाला गया।

जब कोई content लौटा नहीं, vector computation नहीं की गई। अंतिम संग्रह का आधार GitHub मूल रिपॉज़िटरी; निजी search पते, keys और आंतरिक लेख-पाठ public रिपॉज़िटरी में नहीं डाले गए।

## सत्यापन और सीमाएँ

फ़ंक्शन-विवरण आधिकारिक दस्तावेज़ पर आधारित; सभी सॉफ़्टवेयर इंस्टॉल करके नहीं चलाए, एक जैसे model, budget और कथा-विषय से blind evaluation नहीं की। लेखकों के अध्याय-संख्या, मिलियन-शब्द, AI-गंध-हटाने और multi-Agent के प्रचार क्षमता-रैंकिंग में उपयोग नहीं। इस दौर में component-level ablation नहीं किया, इसलिए "मेमोरी हटाने पर गुणवत्ता कितनी गिरी" का निर्णय नहीं दिया जा सकता।

प्रोजेक्ट/seed पूर्णता-जाँच, रैंकिंग boundary test, API विफलता पर पुराने स्नैपशॉट retention test और generated फ़ाइलों की consistency check पूरी। मीट्रिक-मानक का विवरण [methodology.md](methodology.md) में।

सार्वजनिक audit सामग्री:

- [खोज लॉग](../../../research/search-log.json): queries, दौर और result स्टैटिस्टिक्स।
- [संग्रह-निर्णय](../../../research/decisions.json): उपयोग, सीमाएँ, फ़िक्स commit और लाइसेंस सत्यापन।
- [baseline कवरेज](../../../research/coverage.json): 14 संदर्भ लिंक पूरी तरह कवर।
- [प्रारंभिक मीट्रिक](../../../research/initial-metrics.json) और [वर्तमान मीट्रिक](../../../data/metrics.json): प्रारंभिक और जारी अपडेट अलग-अलग।
- [स्थिति](../../../research/status.json) और [पूर्णता-जाँच](../../../research/verification.json): रोकने का कारण और ज्ञात खाली नतीजे।

पूरा स्रोत-पाठ और tool logs local पर ही रहे। सार्वजनिक search statistics में 84 निर्णय और 123 मीट्रिक दर्ज हैं; सामग्री उपरोक्त decisions और snapshots से दोबारा जाँची जा सकती है।
