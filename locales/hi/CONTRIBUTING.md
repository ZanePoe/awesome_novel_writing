# योगदान मार्गदर्िका

नए प्रोजेक्ट जोड़ने, श्रेणी सुधारने या संस्करण- और लाइसेंस-प्रमाण भरने के लिए स्वागत है। कम star अस्वीकृति का कारण नहीं है।

1. `data/projects.json` बदलें; जनरेट की गई README तालिकाएँ हाथ से न एडिट करें।
2. canonical GitHub पता, उपयोग, प्रोजेक्ट का रूप, लागू सीमा और फ़िक्स किए गए commit के प्रमाण-लिंक दें।
3. एक मुख्य श्रेणी चुनें। संलग्न सामान्य-लेखन टूल में उपन्यास से संबंध स्पष्ट हो; सॉफ़्टवेयर, Skill और research benchmark को मिलाया नहीं जाता।
4. implemented, development-preview और roadmap अलग लिखें। मॉडल-प्रभाव, लक्ष्य-शब्दसंख्या और लेखक-स्वयं-रिपोर्ट benchmark को स्वतंत्र परीक्षण-निष्कर्ष नहीं बनाया जाता।
5. लाइसेंस सत्यापित करें; अतिरिक्त वाणिज्यिक शर्तें और लाइसेंस-अंतर यथास्थिति रखें। सार्वजनिक दिखना अपने आप MIT नहीं।
6. fork या पोर्ट तभी अलग प्रविष्टि पाता है जब होस्ट, फ़ंक्शन या मेंटेनेंस-पाथ में व्याख्या-योग्य अंतर हो, और स्रोत-संबंध दर्ज हो।
7. नया प्रोजेक्ट जोड़ने के बाद संपूर्ण मीट्रिक स्नैपशॉट दोबारा लेकर दस्तावेज़ जनरेट करें:

```sh
python scripts/refresh_metrics.py
python scripts/build.py
python -m unittest discover -s tests -v
python scripts/build.py --check
```

`data/seed-references.json` प्रारंभिक संदर्भ प्रोजेक्ट दर्ज करता है; साधारण योगदान में आमतौर पर नहीं बदलता। हर मैन्युअल फ़ंक्शन-सत्यापन पर तारीख़ और evidence commit अपडेट हो; स्वतः star रीफ़्रेश इन फ़ील्ड को अपडेट नहीं करता।

model keys, निजी search पते, अप्रकाशित manuscripts या आंतरिक लेख-पाठ commit न करें। शोध-सारांश `record/YYYY-MM-DD-<चीनी-शीर्षक>.md` में रखे जाते हैं।

## बहुभाषी फ़ाइलें

- `data/projects.json` चीनी में canonical समीक्षा-डेटा है: तथ्य केवल यहाँ एक बार बदले जाते हैं।
- अन्य भाषाओं का पाठ `locales/<lang>/entries.json` (`description`, `boundary`, `license_label`, `license_note`) और `locales/<lang>/ui.json` से आता है; `zh` सीधे `data/projects.json` पर गिरता है, इसलिए `locales/zh/entries.json` नहीं है।
- नया प्रोजेक्ट जोड़ते या positioning, सीमा और लाइसेंस-निष्कर्ष बदलते समय उसी PR में en/es/hi/fr चारों locale पूरे करें, वरना `python scripts/build.py --check` और `python -m unittest discover -s tests -v` फेल होंगे।
- स्थैतिक दस्तावेज़: अंग्रेज़ी रूट की `docs/` और `CONTRIBUTING.md` में, अन्य भाषाएँ `locales/<lang>/` में उसी सापेक्ष पाथ पर। मिरर में सापेक्ष लिंक फ़ाइल की अपनी डायरेक्टरी से resolves होते हैं; repository root की ओर `data/`, `scripts/`, `research/`, `LICENSE`, `record/` को `../../` लिखें। `docs/readme-intro.md` अपवाद है: वह README में inline होता है और भाषा-रूट से resolves होता है।
- `record/` और `research/` मूल भाषा में audit trail हैं; machine-translate नहीं किए जाते।
- जनरेटेड फ़ाइलें (`README.md`, `docs/projects.md`, `docs/rankings.md`, `data/rankings.csv` और हर भाषा-मिरर की उसी नाम की फ़ाइलें) हाथ से न बदलें; वे `python scripts/build.py` से बनती हैं।
