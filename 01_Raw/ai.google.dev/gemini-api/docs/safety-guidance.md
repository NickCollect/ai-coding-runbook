---
source_url: https://ai.google.dev/gemini-api/docs/safety-guidance?hl=id
fetched_at: 2026-09-21T05:52:49.918767+00:00
title: "Panduan keselamatan dan faktualitas \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=id) kini tersedia secara umum. Sebaiknya gunakan API ini untuk mengakses semua fitur dan model terbaru.

![](https://ai.google.dev/_static/images/translated.svg?hl=id)

Google menggunakan teknologi AI untuk menerjemahkan konten ke dalam bahasa pilihan Anda. Terjemahan AI mungkin mengandung kesalahan.

- [Beranda](https://ai.google.dev/?hl=id)
- [Gemini API](https://ai.google.dev/gemini-api?hl=id)
- [Dokumen](https://ai.google.dev/gemini-api/docs?hl=id)

Kirim masukan

# Panduan keselamatan dan faktualitas

Model kecerdasan buatan generatif adalah alat yang canggih, tetapi memiliki keterbatasan. Fleksibilitas dan penerapannya terkadang dapat menghasilkan output yang tidak terduga, seperti output yang tidak akurat, bias, atau menyinggung. Pemrosesan pasca-output, dan evaluasi manual yang ketat sangat penting untuk membatasi risiko bahaya dari output tersebut.

Model yang disediakan oleh Gemini API dapat digunakan untuk berbagai aplikasi AI generatif dan pemrosesan bahasa alami (NLP). Penggunaan fungsi ini hanya tersedia melalui Gemini API atau aplikasi web Google AI Studio. Penggunaan Gemini API oleh Anda juga tunduk pada [Kebijakan Penggunaan Terlarang untuk AI Generatif](https://policies.google.com/terms/generative-ai/use-policy?hl=id) dan [persyaratan layanan Gemini API](https://ai.google.dev/terms?hl=id).

Sebagian dari hal yang membuat model bahasa besar (LLM) sangat berguna adalah karena model ini merupakan alat kreatif yang dapat menangani berbagai tugas bahasa. Sayangnya,
hal ini juga berarti bahwa model bahasa besar dapat menghasilkan output yang tidak
Anda harapkan, termasuk teks yang menyinggung, tidak sensitif, atau salah secara faktual.
Selain itu, fleksibilitas model ini yang luar biasa juga menyulitkan
memprediksi dengan tepat jenis output yang tidak diinginkan yang mungkin dihasilkan. Meskipun
Gemini API telah dirancang dengan mempertimbangkan [prinsip AI Google](https://ai.google/principles/?hl=id), developer bertanggung jawab untuk
menerapkan model ini secara bertanggung jawab. Untuk membantu developer membuat aplikasi yang aman dan bertanggung jawab, Gemini API memiliki beberapa pemfilteran konten bawaan serta setelan keamanan yang dapat disesuaikan di 4 dimensi bahaya. Baca panduan
[setelan keamanan](https://ai.google.dev/gemini-api/docs/safety-settings?hl=id) untuk mempelajari lebih lanjut. Fitur ini juga menawarkan Perujukan dengan Google Penelusuran yang diaktifkan untuk meningkatkan faktualitas, meskipun fitur ini dapat dinonaktifkan bagi developer yang kasus penggunaannya lebih kreatif dan tidak mencari informasi.

Dokumen ini dimaksudkan untuk memperkenalkan beberapa risiko keamanan yang dapat muncul saat
menggunakan LLM, dan merekomendasikan desain dan pengembangan keamanan yang baru muncul. (Perhatikan bahwa hukum dan peraturan juga dapat memberlakukan batasan, tetapi pertimbangan tersebut berada di luar cakupan panduan ini.)

Langkah-langkah berikut direkomendasikan saat membangun aplikasi dengan LLM:

- Memahami risiko keamanan aplikasi Anda
- Mempertimbangkan penyesuaian untuk mengurangi risiko keselamatan
- Melakukan pengujian keamanan yang sesuai dengan kasus penggunaan Anda
- Meminta masukan dari pengguna dan memantau penggunaan

Fase penyesuaian dan pengujian harus dilakukan secara berulang hingga Anda mencapai performa yang sesuai untuk aplikasi Anda.

![Siklus penerapan model](https://ai.google.dev/static/gemini-api/docs/images/safety_diagram.png?hl=id)

## Memahami risiko keamanan aplikasi Anda

Dalam konteks ini, keamanan didefinisikan sebagai kemampuan LLM untuk menghindari menyebabkan bahaya bagi penggunanya, misalnya, dengan membuat bahasa atau konten berbahaya yang mempromosikan stereotipe. Model yang tersedia melalui Gemini API telah dirancang dengan mempertimbangkan [prinsip AI Google](https://ai.google/principles/?hl=id) dan penggunaan model ini tunduk pada [Kebijakan Penggunaan Terlarang untuk AI Generatif](https://policies.google.com/terms/generative-ai/use-policy?hl=id). API ini menyediakan filter keamanan bawaan untuk membantu mengatasi beberapa masalah umum model bahasa seperti bahasa berbahaya dan ujaran kebencian, serta berupaya untuk inklusivitas dan menghindari stereotipe. Namun, setiap aplikasi dapat menimbulkan serangkaian risiko yang berbeda bagi penggunanya. Jadi, sebagai pemilik aplikasi, Anda bertanggung jawab untuk mengetahui pengguna Anda dan potensi bahaya yang dapat ditimbulkan oleh aplikasi Anda, serta memastikan bahwa aplikasi Anda menggunakan LLM secara aman dan bertanggung jawab.

Sebagai bagian dari penilaian ini, Anda harus mempertimbangkan kemungkinan terjadinya bahaya dan menentukan keseriusan serta langkah-langkah mitigasinya. Misalnya, aplikasi yang membuat esai berdasarkan peristiwa faktual harus lebih berhati-hati dalam menghindari misinformasi, dibandingkan dengan aplikasi yang membuat cerita fiksi untuk hiburan. Cara yang baik untuk mulai mempelajari potensi risiko keselamatan adalah dengan meneliti pengguna akhir Anda, dan orang lain yang mungkin terpengaruh oleh hasil aplikasi Anda. Hal ini dapat dilakukan dalam berbagai bentuk, termasuk meneliti studi terbaru di domain aplikasi Anda, mengamati cara orang menggunakan aplikasi serupa, atau menjalankan studi pengguna, survei, atau melakukan wawancara informal dengan calon pengguna.

### Tips lanjutan

- Bicaralah dengan beragam calon pengguna dalam target populasi Anda tentang aplikasi Anda dan tujuan yang dimaksudkan agar mendapatkan perspektif yang lebih luas tentang potensi risiko dan menyesuaikan kriteria keberagaman sesuai kebutuhan.
- [AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) yang dirilis oleh National Institute of Standards and Technology (NIST) pemerintah Amerika Serikat memberikan panduan yang lebih mendetail dan sumber pembelajaran tambahan untuk manajemen risiko AI.
- Publikasi DeepMind tentang [risiko bahaya etis dan sosial dari model bahasa](https://arxiv.org/abs/2112.04359) menjelaskan secara mendetail cara aplikasi model bahasa dapat menyebabkan bahaya.

## Mempertimbangkan penyesuaian untuk mengurangi risiko keselamatan dan faktualitas

Setelah memahami risiko, Anda dapat memutuskan cara memitigasinya. Menentukan risiko mana yang harus diprioritaskan dan seberapa besar upaya yang harus Anda lakukan untuk mencoba mencegahnya adalah keputusan penting, mirip dengan memilah-milah bug dalam proyek software. Setelah menentukan prioritas, Anda dapat mulai memikirkan jenis mitigasi yang paling tepat. Sering kali perubahan sederhana dapat
membuat perbedaan dan mengurangi risiko.

Misalnya, saat mendesain aplikasi, pertimbangkan:

- **Menyesuaikan output model** agar lebih mencerminkan apa yang dapat diterima dalam konteks aplikasi Anda. Penyesuaian dapat membuat output model lebih
  dapat diprediksi dan konsisten, sehingga dapat membantu mengurangi risiko tertentu.
- **Menyediakan metode input yang memfasilitasi output yang lebih aman.** Input persis yang Anda berikan ke LLM dapat memengaruhi kualitas output.
  Bereksperimen dengan perintah input untuk menemukan perintah yang paling aman dalam kasus penggunaan Anda sangatlah bermanfaat, karena Anda kemudian dapat memberikan UX yang memfasilitasinya. Misalnya, Anda dapat membatasi pengguna untuk memilih hanya dari
  daftar drop-down perintah input, atau menawarkan saran pop-up dengan
  frasa
  deskriptif yang Anda temukan berperforma aman dalam konteks aplikasi Anda.
- **Memblokir input yang tidak aman dan memfilter output sebelum ditampilkan kepada
  pengguna.** Dalam situasi sederhana, daftar yang tidak diizinkan dapat digunakan untuk mengidentifikasi dan memblokir kata atau frasa yang tidak aman dalam perintah atau respons, atau mewajibkan peninjau manual untuk mengubah atau memblokir konten tersebut secara manual.
- **Menggunakan pengklasifikasi terlatih untuk memberi label setiap perintah dengan sinyal berpotensi berbahaya atau adversarial.** Kemudian, berbagai strategi dapat diterapkan untuk menangani permintaan berdasarkan jenis bahaya yang terdeteksi. Misalnya, jika input bersifat terlalu adversarial atau melanggar, input tersebut dapat diblokir dan menghasilkan respons yang telah ditulis dalam skrip.
  **Tips lanjutan:** Jika sinyal menentukan bahwa output berbahaya, aplikasi dapat menggunakan opsi berikut:

  - Menyediakan pesan error atau output yang telah ditulis dalam skrip.
  - Coba lagi perintahnya, jika output alternatif yang aman dihasilkan, karena terkadang perintah yang sama akan menghasilkan output yang berbeda.
- **Menerapkan pengamanan terhadap penyalahgunaan yang disengaja** seperti menetapkan ID unik untuk setiap pengguna dan membatasi volume kueri pengguna yang dapat dikirimkan dalam jangka waktu tertentu. Pengamanan lainnya adalah mencoba dan
  melindungi dari kemungkinan injeksi perintah. Injeksi perintah, seperti injeksi SQL, adalah cara bagi pengguna berbahaya untuk mendesain perintah input yang memanipulasi output model, misalnya, dengan mengirimkan perintah input yang menginstruksikan model untuk mengabaikan contoh sebelumnya. Lihat
  [Kebijakan Penggunaan Terlarang untuk AI Generatif](https://policies.google.com/terms/generative-ai/use-policy?hl=id)
  untuk mengetahui detail tentang penyalahgunaan yang disengaja.
- **Menyesuaikan fungsi menjadi sesuatu yang pada dasarnya memiliki risiko lebih rendah.**
  Tugas yang lebih sempit cakupannya (misalnya, mengekstrak kata kunci dari bagian
  teks) atau yang memiliki pengawasan manusia yang lebih besar (misalnya, membuat konten
  singkat yang akan ditinjau oleh manusia), sering kali menimbulkan risiko yang lebih rendah. Jadi, misalnya, daripada membuat aplikasi untuk menulis balasan email dari awal, Anda dapat membatasinya untuk memperluas kerangka atau menyarankan susunan kata alternatif.
- **Menyesuaikan setelan keamanan konten berbahaya untuk mengurangi kemungkinan Anda
  melihat respons yang dapat berbahaya.** Gemini API menyediakan setelan keamanan
  yang dapat Anda sesuaikan selama tahap pembuatan prototipe untuk menentukan apakah
  aplikasi Anda memerlukan konfigurasi keamanan yang lebih ketat atau longgar. Anda dapat
  menyesuaikan setelan ini di lima kategori filter untuk membatasi atau mengizinkan
  jenis konten tertentu. Lihat [panduan setelan keamanan](https://ai.google.dev/gemini-api/docs/safety-settings?hl=id) untuk mempelajari setelan keamanan yang dapat disesuaikan yang tersedia melalui Gemini API.
- **Mengurangi potensi ketidakakuratan faktual atau halusinasi dengan mengaktifkan
  Perujukan dengan Google Penelusuran**. Ingat, banyak model AI bersifat eksperimental
  dan dapat menyajikan informasi yang faktanya tidak akurat, berhalusinasi, atau
  menghasilkan output yang bermasalah. Fitur Grounding with Google Search menghubungkan model Gemini ke konten web real-time dan berfungsi dengan semua bahasa yang tersedia. Dengan fitur ini, Gemini dapat memberikan jawaban yang lebih akurat dan mengutip sumber yang dapat diverifikasi di luar batas informasinya.

## Melakukan pengujian keamanan yang sesuai dengan kasus penggunaan Anda

Pengujian adalah bagian penting dalam membangun aplikasi yang andal dan aman, tetapi tingkat, cakupan, dan strategi pengujian akan bervariasi. Misalnya, generator haiku yang hanya untuk bersenang-senang cenderung menimbulkan risiko yang tidak terlalu parah dibandingkan, misalnya, aplikasi yang dirancang untuk digunakan oleh firma hukum guna meringkas dokumen hukum dan membantu menyusun kontrak. Namun, generator haiku dapat digunakan oleh berbagai pengguna yang lebih luas, yang berarti potensi upaya berbahaya atau bahkan input berbahaya yang tidak disengaja dapat lebih besar. Konteks penerapan juga penting. Misalnya, aplikasi dengan output yang ditinjau oleh pakar manusia sebelum tindakan apa pun diambil mungkin dianggap lebih kecil kemungkinannya menghasilkan output berbahaya dibandingkan aplikasi identik tanpa pengawasan tersebut.

Tidak jarang Anda harus melakukan beberapa iterasi perubahan dan pengujian sebelum merasa yakin bahwa Anda siap meluncurkan aplikasi, bahkan untuk aplikasi yang risikonya relatif rendah. Dua jenis pengujian sangat berguna untuk aplikasi AI:

- **Tolok ukur keamanan** melibatkan perancangan metrik keamanan yang mencerminkan cara aplikasi Anda dapat menjadi tidak aman dalam konteks kemungkinan penggunaannya, lalu menguji seberapa baik performa aplikasi Anda berdasarkan metrik tersebut menggunakan set data evaluasi. Sebaiknya pikirkan tingkat minimum metrik keamanan yang dapat diterima sebelum melakukan pengujian sehingga 1) Anda dapat mengevaluasi hasil pengujian berdasarkan ekspektasi tersebut dan 2) Anda dapat mengumpulkan set data evaluasi berdasarkan pengujian yang mengevaluasi metrik yang paling penting bagi Anda.

  **Tips lanjutan:**

  - Berhati-hatilah agar tidak terlalu mengandalkan pendekatan “siap pakai” karena kemungkinan Anda perlu membuat set data pengujian sendiri menggunakan pemberi rating manusia agar sesuai sepenuhnya dengan konteks aplikasi Anda.
  - Jika memiliki lebih dari satu metrik, Anda harus memutuskan cara melakukan trade-off jika perubahan menyebabkan peningkatan pada satu metrik dan penurunan pada metrik lainnya. Seperti halnya teknik performa lainnya, Anda mungkin ingin berfokus pada performa terburuk di seluruh set evaluasi, bukan performa rata-rata.
- **Pengujian adversarial** secara proaktif mencoba merusak aplikasi Anda. Tujuannya adalah untuk mengidentifikasi titik lemah sehingga Anda dapat mengambil langkah-langkah untuk memperbaikinya sebagaimana mestinya. Pengujian adversarial dapat memerlukan waktu/upaya yang signifikan dari evaluator dengan keahlian di aplikasi Anda, tetapi makin sering Anda melakukannya, makin besar peluang Anda untuk menemukan masalah, terutama yang jarang terjadi atau hanya terjadi setelah aplikasi dijalankan berulang kali.

  - Pengujian adversarial adalah metode untuk mengevaluasi model ML secara sistematis dengan maksud mempelajari perilakunya saat diberi input berbahaya atau yang tidak sengaja membahayakan:
    - Input dapat dianggap berbahaya jika input tersebut jelas dirancang untuk
      menghasilkan output yang tidak aman atau berbahaya--misalnya, meminta model
      pembuatan teks untuk membuat ujaran kebencian tentang agama tertentu.
    - Input tidak sengaja membahayakan jika input itu sendiri mungkin tampak aman, tetapi menghasilkan output yang membahayakan -- misalnya, meminta model pembuatan teks untuk mendeskripsikan seseorang dari etnis tertentu dan menerima output yang bersifat rasis.
  - Yang membedakan pengujian adversarial dari evaluasi standar adalah komposisi data yang digunakan untuk pengujian. Untuk pengujian adversarial, pilih data pengujian yang kemungkinan besar akan memicu output bermasalah dari model. Hal ini berarti menyelidiki perilaku model untuk semua jenis bahaya yang mungkin terjadi, termasuk contoh langka atau tidak biasa dan kasus ekstrem yang relevan dengan kebijakan keamanan. Hal ini juga harus mencakup
    keberagaman dalam berbagai dimensi kalimat seperti struktur,
    makna, dan panjang. Anda dapat melihat [praktik AI Bertanggung Jawab Google dalam
    keterbukaan](https://ai.google/responsibilities/responsible-ai-practices/?category=fairness&hl=id)
    untuk mengetahui detail selengkapnya tentang hal yang perlu dipertimbangkan saat membuat set data pengujian.
    **Tips lanjutan:**
  - Gunakan [pengujian otomatis](https://www.deepmind.com/blog/red-teaming-language-models-with-language-models?hl=id), bukan metode tradisional dengan merekrut orang ke dalam 'tim merah' untuk mencoba merusak aplikasi Anda. Dalam pengujian otomatis, 'red team' adalah model bahasa lain yang menemukan teks input yang memicu output berbahaya dari model yang sedang diuji.

## Memantau masalah

Tidak peduli seberapa banyak Anda menguji dan memitigasi, Anda tidak akan pernah dapat menjamin kesempurnaan, jadi rencanakan terlebih dahulu cara Anda akan menemukan dan mengatasi masalah yang muncul. Pendekatan umum mencakup menyiapkan saluran yang dipantau agar pengguna dapat membagikan masukan (misalnya, rating suka/tidak suka) dan menjalankan studi pengguna untuk secara proaktif meminta masukan dari beragam pengguna, terutama jika pola penggunaan berbeda dari yang diharapkan.

### Tips lanjutan

- Saat pengguna memberikan masukan ke produk AI, hal ini dapat meningkatkan performa AI dan pengalaman pengguna seiring waktu, misalnya, dengan membantu Anda memilih contoh yang lebih baik untuk penyesuaian perintah. [Bab Masukan dan Kontrol](https://pair.withgoogle.com/chapter/feedback-controls/) dalam [Panduan Google untuk Orang dan AI](https://pair.withgoogle.com/guidebook/chapters) menggarisbawahi pertimbangan utama yang harus diperhatikan saat mendesain mekanisme masukan.

## Langkah berikutnya

- Lihat panduan
  [setelan keamanan](https://ai.google.dev/gemini-api/docs/safety-settings?hl=id) untuk mempelajari setelan keamanan yang dapat disesuaikan yang tersedia melalui Gemini API.
- Lihat [pengantar perintah](https://ai.google.dev/gemini-api/docs/prompting-intro?hl=id) untuk mulai menulis perintah pertama Anda.

Kirim masukan

Kecuali dinyatakan lain, konten di halaman ini dilisensikan berdasarkan [Lisensi Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), sedangkan contoh kode dilisensikan berdasarkan [Lisensi Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Untuk mengetahui informasi selengkapnya, lihat [Kebijakan Situs Google Developers](https://developers.google.com/site-policies?hl=id). Java adalah merek dagang terdaftar dari Oracle dan/atau afiliasinya.

Terakhir diperbarui pada 2026-06-05 UTC.

Ada masukan untuk kami?

[[["Mudah dipahami","easyToUnderstand","thumb-up"],["Memecahkan masalah saya","solvedMyProblem","thumb-up"],["Lainnya","otherUp","thumb-up"]],[["Informasi yang saya butuhkan tidak ada","missingTheInformationINeed","thumb-down"],["Terlalu rumit/langkahnya terlalu banyak","tooComplicatedTooManySteps","thumb-down"],["Sudah usang","outOfDate","thumb-down"],["Masalah terjemahan","translationIssue","thumb-down"],["Masalah kode / contoh","samplesCodeIssue","thumb-down"],["Lainnya","otherDown","thumb-down"]],["Terakhir diperbarui pada 2026-06-05 UTC."],[],[]]
