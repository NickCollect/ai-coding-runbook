---
source_url: https://ai.google.dev/gemini-api/docs/troubleshoot-ai-studio?hl=id
fetched_at: 2026-06-01T05:57:05.406714+00:00
title: "Memecahkan masalah Google AI Studio \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Deep Research Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=id) kini tersedia dalam pratinjau dengan perencanaan kolaboratif, visualisasi, dukungan MCP, dan lainnya.

![](https://ai.google.dev/_static/images/translated.svg?hl=id)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Beranda](https://ai.google.dev/?hl=id)
- [Gemini API](https://ai.google.dev/gemini-api?hl=id)
- [Dokumen](https://ai.google.dev/gemini-api/docs?hl=id)

Kirim masukan

# Memecahkan masalah Google AI Studio

Halaman ini memberikan saran untuk memecahkan masalah Google AI Studio jika Anda
mengalami masalah.

## Memahami error 403 Akses Dibatasi

Jika Anda melihat error 403 Akses Dibatasi, Anda menggunakan Google AI Studio dengan cara yang tidak mematuhi [Persyaratan Layanan](https://ai.google.dev/terms?hl=id). Salah satu alasan umumnya adalah Anda tidak berada di [wilayah yang didukung](https://ai.google.dev/available_regions?hl=id).

## Menyelesaikan respons Tanpa Konten di Google AI Studio

Pesan warning **Tidak Ada Konten** muncul di
Google AI Studio jika konten diblokir karena alasan apa pun. Untuk melihat detail selengkapnya,
arahkan kursor ke **Tidak Ada Konten** dan klik
warning **Keamanan**.

Jika respons diblokir karena [setelan keamanan](https://ai.google.dev/docs/safety_setting?hl=id) dan
Anda mempertimbangkan [risiko keamanan](https://ai.google.dev/docs/safety_guidance?hl=id) untuk kasus penggunaan Anda, Anda
dapat mengubah
[setelan keamanan](https://ai.google.dev/docs/safety_setting?hl=id#safety_settings_in_makersuite)
untuk memengaruhi respons yang ditampilkan.

Jika respons diblokir, tetapi bukan karena setelan keamanan, kueri atau respons mungkin melanggar [Persyaratan Layanan](https://ai.google.dev/terms?hl=id) atau tidak didukung.

## Memeriksa penggunaan dan batas token

Saat Anda membuka perintah, tombol **Pratinjau Teks** di bagian bawah layar akan menampilkan token saat ini yang digunakan untuk konten perintah Anda dan jumlah token maksimum untuk model yang digunakan.

## Izin IAM Google Cloud untuk AI Studio

Anggota project Google Cloud memerlukan izin Identity and Access Management (IAM) tertentu untuk melakukan tindakan di Google AI Studio. Untuk mengetahui informasi selengkapnya tentang identitas ini, lihat [Ringkasan principal IAM](https://cloud.google.com/iam/docs/principals?hl=id).

Pengguna dengan peran **Editor** atau **Pemilik** di project Google Cloud terkait memiliki izin penuh untuk melihat dasbor dan mengelola kunci API Gemini. Pengguna dengan peran **Pelihat** dapat melihat dasbor dan kunci API, tetapi tidak dapat membuat, memperbarui, atau menghapusnya.

Untuk kontrol yang lebih terperinci, lihat tabel berikut untuk mengetahui izin spesifik yang diperlukan untuk setiap fitur AI Studio. Untuk mengetahui petunjuk tentang cara memberikan izin ini, lihat [Memberikan, mengubah, dan mencabut akses ke resource](https://cloud.google.com/iam/docs/granting-changing-revoking-access?hl=id) dalam dokumentasi Google Cloud.

| Fitur AI Studio | Izin IAM yang diperlukan | Persyaratan tambahan |
| --- | --- | --- |
| **Telusuri project** (impor project) | `resourcemanager.projects.get` |  |
| **Mengganti nama project** | `resourcemanager.projects.update` |  |
| **Menampilkan tingkat kuota** | T/A |  |
| **Buat kunci API** | Memiliki izin **Cari project**, dan:  `apikeys.keys.create` `serviceusage.services.enable` `iam.serviceAccountApiKeyBindings.create` `iam.serviceAccounts.create` |  |
| **Mencantumkan kunci API** | Memiliki izin **Telusuri project**, dan:  `apikeys.keys.list` `serviceusage.services.get` | Project Google Cloud harus mengaktifkan [Generative Language API](https://console.cloud.google.com/apis/library/generativelanguage.googleapis.com?hl=id). |
| **Mengganti nama kunci API** | `apikeys.keys.update` |  |
| **Menghapus kunci API** | `apikeys.keys.delete` |  |
| **Dasbor penggunaan** | Memiliki izin **Cari project**, dan:  `monitoring.timeSeries.list` |  |
| **Dasbor batas kecepatan** | Memiliki izin **Dasbor penggunaan**, dan:  `cloudquotas.quotas.get` |  |
| **Pengeluaran (Batas penagihan)** | `billing.resourceCosts.get` (untuk melihat pembelanjaan) `billing.resourcebudgets.read` (untuk melihat batas) `billing.resourcebudgets.write` (untuk menetapkan batas) |  |
| **Dasbor penagihan** | `billing.accounts.get` |  |

### Pemeriksaan akses lainnya

Selain izin IAM Google Cloud, AI Studio juga melakukan pemeriksaan keamanan dan kepatuhan. Anda mungkin mengalami error `PERMISSION_DENIED` atau error pembatasan akses di antarmuka AI Studio atau dalam respons API jika Anda tidak memenuhi persyaratan berikut:

- **Pemeriksaan keamanan:** Permintaan Anda harus lulus pemeriksaan keamanan otomatis.
- **Persyaratan Layanan:** Anda harus menyetujui Persyaratan Layanan Google dan Persyaratan Layanan Tambahan AI Generatif.
- **Wilayah yang didukung:** Anda harus berada di [wilayah yang didukung](https://ai.google.dev/gemini-api/docs/available-regions?hl=id).
- **Kepercayaan & Keamanan:** Project Google Cloud tidak boleh ditandai karena penyalahgunaan.

Kirim masukan

Kecuali dinyatakan lain, konten di halaman ini dilisensikan berdasarkan [Lisensi Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), sedangkan contoh kode dilisensikan berdasarkan [Lisensi Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Untuk mengetahui informasi selengkapnya, lihat [Kebijakan Situs Google Developers](https://developers.google.com/site-policies?hl=id). Java adalah merek dagang terdaftar dari Oracle dan/atau afiliasinya.

Terakhir diperbarui pada 2026-05-29 UTC.

Ada masukan untuk kami?

[[["Mudah dipahami","easyToUnderstand","thumb-up"],["Memecahkan masalah saya","solvedMyProblem","thumb-up"],["Lainnya","otherUp","thumb-up"]],[["Informasi yang saya butuhkan tidak ada","missingTheInformationINeed","thumb-down"],["Terlalu rumit/langkahnya terlalu banyak","tooComplicatedTooManySteps","thumb-down"],["Sudah usang","outOfDate","thumb-down"],["Masalah terjemahan","translationIssue","thumb-down"],["Masalah kode / contoh","samplesCodeIssue","thumb-down"],["Lainnya","otherDown","thumb-down"]],["Terakhir diperbarui pada 2026-05-29 UTC."],[],[]]
