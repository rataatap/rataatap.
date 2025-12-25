<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Rataatap Studio</title>
  <style>
    :root {
      --black: #0e0e0e;
      --white: #ffffff;
      --gray: #f2f2f2;
    }
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
      font-family: 'Segoe UI', sans-serif;
    }
    body {
      background: var(--white);
      color: var(--black);
      line-height: 1.6;
    }
    header {
      background: var(--black);
      color: var(--white);
      padding: 60px 20px;
      text-align: center;
    }
    header img {
      max-width: 180px;
      margin-bottom: 20px;
    }
    section {
      padding: 80px 10%;
    }
    h2 {
      text-align: center;
      margin-bottom: 40px;
      letter-spacing: 2px;
    }
    .about {
      max-width: 900px;
      margin: auto;
      text-align: center;
    }
    .team {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
      gap: 30px;
    }
    .card {
      background: var(--gray);
      padding: 20px;
      text-align: center;
      border-radius: 8px;
    }
    .card img {
      width: 100%;
      border-radius: 8px;
      margin-bottom: 15px;
    }
    .portfolio {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
      gap: 20px;
    }
    .portfolio img {
      width: 100%;
      border-radius: 8px;
    }
    .category {
      margin-bottom: 60px;
    }
    footer {
      background: var(--black);
      color: var(--white);
      padding: 40px 20px;
      text-align: center;
    }
    .socials a {
      margin: 0 10px;
      color: var(--white);
      text-decoration: none;
      font-weight: bold;
    }
  </style>
</head>
<body>

<header>
  <img src="LOGO-RATAATAP.png" alt="Rataatap Studio Logo" />
  <h1>RATAATAP STUDIO</h1>
  <p>Architecture & Interior Design</p>
</header>

<section id="about">
  <h2>TENTANG KAMI</h2>
  <div class="about">
    <p>
      Rataatap adalah jasa desain arsitektural dan desain interior yang bergerak di bidang desain gambar.
      Rataatap didirikan pada 11 November 2025 dengan tujuan membangun jasa desain yang murah namun
      berkualitas tinggi.
    </p>
    <br />
    <p>
      Visi dan misi Rataatap Studio adalah menjunjung tinggi kualitas, kreativitas, teknologi, serta riset
      terhadap perkembangan arsitektur di Indonesia maupun luar negeri.
      Target ke depan, Rataatap Studio diharapkan menjadi salah satu konsultan terbaik di Jawa Timur.
    </p>
  </div>
</section>

<section id="team">
  <h2>TEAM DESIGN</h2>
  <div class="team">
    <div class="card">
      <img src="fotozidan.jpg.jpeg" alt="Head Office" />
      <h4>Head Office</h4>
      <p>Zidan</p>
    </div>
    <div class="card">
      <img src="fotoilham.jpg.jpeg" alt="Desainer Arsitek" />
      <h4>Desainer Arsitek</h4>
      <p>Ilham</p>
    </div>
    <div class="card">
      <img src="fotoeko.jpg.jpeg" alt="Civil Engineer" />
      <h4>Civil Engineer</h4>
      <p>Eko</p>
    </div>
    <div class="card">
      <img src="fotoridwan.jpg.jpeg" alt="Interior Designer" />
      <h4>Interior Designer</h4>
      <p>Ridwan</p>
    </div>
  </div>
</section>

<section id="portfolio">
  <h2>PORTOFOLIO</h2>

  <div class="category">
    <h3>Rumah Classic</h3>
    <div class="portfolio">
      <img src="RENDER-CLASIC.jpeg" />
      <img src="RENDER-INTERIOR-CLASIC.jpeg" />
    </div>
  </div>

  <div class="category">
    <h3>Modern Minimalis</h3>
    <div class="portfolio">
      <img src="RENDER-MODEREN-MINIMALIS.jpeg" />
      <img src="RENDER-MODEREN-INTERIOR (1).jpeg" />
    </div>
  </div>

  <div class="category">
    <h3>Modern Kontemporer</h3>
    <div class="portfolio">
      <img src="RENDER-MODEREN-KONTEMPORER.jpeg" />
      <img src="RENDER-INTERIOR-KONTEMPORER.jpeg" />
    </div>
  </div>

  <div class="category">
    <h3>Scandinavian</h3>
    <div class="portfolio">
      <img src="RENDER-SCANDINAVIAN.jpeg" />
      <img src="RENDER-INTERIOR-SCANDINAVIAN (1).jpeg" />
    </div>
  </div>

  <div class="category">
    <h3>Futuristic</h3>
    <div class="portfolio">
      <img src="RENDER-FUTURISTIK.jpeg" />
      <img src="RENDER-FUTURISTIK-INTERIOR.jpeg" />
    </div>
  </div>

  <div class="category">
    <h3>Industrial</h3>
    <div class="portfolio">
      <img src="RENDER-INDUSTRIAL.jpeg" />
      <img src="RENDER-INTERIOR-INDUSTRIAL.jpeg" />
    </div>
  </div>
</section>

<footer>
  <h3>MEDIA SOSIAL</h3>
  <div class="socials">
    <a href="https://www.instagram.com/rataatap">Instagram</a>
    <a href="https://api.whatsapp.com/send/?phone=%2B6282245078169&text&type=phone_number&app_absent=0"">WhatsApp</a>
    <a href="https://www.tiktok.com/@rataatap.studio?_r=1&_t=ZS-92WR7u5iA6y">TikTok</a>
    <a href="https://www.youtube.com/@rataatapstudio">YouTube</a>
    <a href="#">Shopee</a>
  </div>
  <p style="margin-top:20px; font-size:14px;">© 2025 Rataatap Studio</p>
</footer>

</body>
</html>
