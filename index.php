<?php require_once("admin/common.php"); ?>
<!DOCTYPE html>
<html lang="<?php echo $lang['langcode'] ?>">
<head>
  <!-- PORTED BY JUPITER for orangepizero3 specifications -->
  <meta charset="utf-8">
  <title>Global Hope - Home</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="css/offline.css?v=<?php echo date('Ymd-His'); ?>">
</head>
<body class="page-body">

  <!-- Header -->
  <header class="site-header">
    <div class="wrap header-inner">


      <a href="index.php" class="brand">
      <img src="art/dream_cube_logo.png" alt="Global Hope Logo" style="height:40px;">
      </a>


      <nav class="main-nav">
        <a href="index.php"><?php echo strtoupper($lang['home']) ?></a>
        <a href="about-dreamcube.php"><?php echo strtoupper($lang['about']) ?></a>


        <div class="nav-dropdown">
          <a href="http://<?php echo $_SERVER['SERVER_ADDR']; ?>:81/" target="_blank" class="dropdown-toggle">KIWIX</a>
          <div class="dropdown-menu">

          <?php


            $feedXml = simplexml_load_file('/var/www/scripts/kiwix_feeds.xml');
            if ($feedXml && isset($feedXml->entry)) {
                foreach ($feedXml->entry as $entry) {
                    $title = (string)$entry->title;
                    $link = '';
                    foreach ($entry->link as $l) {
                        if ($l['type'] == 'text/html') {
                            $link = (string)$l['href'];
                            break;
                        }
                    }
                    if ($title && $link) {
                        echo '<a href="http://'.$_SERVER['SERVER_ADDR'].':81' . htmlspecialchars($link) . '" target="_blank">' . htmlspecialchars($title) . '</a>';
                    }
                }
            }

          

          ?>
          </div>
        </div>


        <div class="nav-dropdown">
          <a href="http://<?php echo $_SERVER['SERVER_ADDR']; ?>:8080/en/learn/#/home/" target="_blank" class="dropdown-toggle">KOLIBRI</a>
          <div class="dropdown-menu">
            <a href="http://<?php echo $_SERVER['SERVER_ADDR']; ?>:8080/en/learn/#/topics/t/c9d7f950ab6b5a1199e3d6c10d7f0103/folders?last=HOME" target="_blank">Khan Academy</a>
            <a href="http://<?php echo $_SERVER['SERVER_ADDR']; ?>:8080/en/learn/#/topics/t/0418cc231e9c5513af0fff9f227f7172/folders?last=HOME" target="_blank">Hello Channel</a>
            <a href="http://<?php echo $_SERVER['SERVER_ADDR']; ?>:8080/en/learn/#/topics/t/197934f144305350b5820c7c4dd8e194/folders?last=HOME" target="_blank">PhET Interactive</a>
            <a href="http://<?php echo $_SERVER['SERVER_ADDR']; ?>:8080/en/learn/#/topics/t/2d7b056d668a58ee9244ccf76108cbdb/folders?last=HOME" target="_blank">Book Dash</a>
          </div>
        </div>
        <?php

        
        ?>


        <a href="admin/modules.php" class="admin-link"><?php echo $lang['admin'] ?></a>
      </nav>
      <button class="nav-toggle" aria-hidden="true">☰</button>
    </div>
  </header>

<!-- Hero -->
<section class="hero hero-animated">
  <div class="hero-image" style="text-align:center;">
  <img src="art/dream_cube_transparent.png" alt="DreamCube Banner" style="width:100%;max-width:280px;border-radius:16px;">
  </div>
  <div class="hero-inner">
    <h1 class="hero-title">Welcome to DreamCube</h1>
    <p class="hero-sub">Empowering communities with education — anytime, anywhere, even without the internet.</p>
    <button class="hero-cta" onclick="document.getElementById('platform-section').scrollIntoView({behavior: 'smooth'});">Start Now</button>
  </div>
</section>


<section class="section platform-section" id="platform-section">
  <div class="wrap">
    <h2 class="section-title">Explore Platforms</h2>
    <div class="platform-row">
      <div class="platform-item">
        <img src="art/rachel.png" alt="Rachel" class="platform-thumb"  onclick="document.getElementById('search-section').scrollIntoView({behavior: 'smooth'});">
        <p class="platform-name">Rachel</p>
      </div>
      <div class="platform-item">
        <a href="http://<?php echo $_SERVER['SERVER_ADDR']; ?>:81/" target="_blank">
        <img src="art/kiwix.png" alt="Kiwix" class="platform-thumb">
        </a>
        <p class="platform-name">Kiwix</p>
      </div>
      <div class="platform-item">
        <a href="http://<?php echo $_SERVER['SERVER_ADDR']; ?>:8080/en/learn/#/home/" target="_blank">
        <img src="art/kolibri.png" alt="Kolibri" class="platform-thumb">
        </a>
        <p class="platform-name">Kolibri</p>
      </div>
    </div>
  </div>
</section>



<!-- Add this after the platform-section -->
<section class="section resource-section" id="resource-section">
  <div class="wrap">
    <h2 class="section-title">Explore Featured Modules</h2>
    <div class="platform-row">
      <div class="platform-item">
        <a href="http://<?php echo $_SERVER['SERVER_ADDR']; ?>:81/en_wikipedia_for_schools_2013/A/index.htm" target="_blank">
          <img src="art/wikipedia.png" alt="Wikipedia" class="platform-thumb">
        </a>
        <p class="platform-name">Wikipedia</p>
      </div>
      <div class="platform-item">
        <a href="http://<?php echo $_SERVER['SERVER_ADDR']; ?>:8080/en/learn/#/topics/t/c9d7f950ab6b5a1199e3d6c10d7f0103/folders?last=HOME" target="_blank">
          <img src="art/khan.png" alt="Khan Academy" class="platform-thumb">
        </a>
        <p class="platform-name">Khan Academy</p>
      </div>
      <div class="platform-item">
        <a href="http://<?php echo $_SERVER['SERVER_ADDR']; ?>:8080/en/learn/#/topics/t/0418cc231e9c5513af0fff9f227f7172/folders?last=HOME" target="_blank">
          <img src="art/hellochannel.png" alt="Hello Channel" class="platform-thumb">
        </a>
        <p class="platform-name">Hello Channel</p>
      </div>
      <div class="platform-item">
        <a href="http://<?php echo $_SERVER['SERVER_ADDR']; ?>:8080/en/learn/#/topics/t/197934f144305350b5820c7c4dd8e194/folders?last=HOME" target="_blank">
          <img src="art/phet.png" alt="PhET Interactive Simulations" class="platform-thumb">
        </a>
        <p class="platform-name">PhET Interactive</p>
      </div>
      <div class="platform-item">
        <a href="http://<?php echo $_SERVER['SERVER_ADDR']; ?>:8080/en/learn/#/topics/t/2d7b056d668a58ee9244ccf76108cbdb/folders?last=HOME" target="_blank">
          <img src="art/bookdash.png" alt="Book Dash" class="platform-thumb">
        </a>
        <p class="platform-name">Book Dash</p>
      </div>
    </div>
  </div>
</section>


  <!-- Search -->
  <section class="wrap section" id="search-section">
    <form class="search-form" action="#" method="get" style="display:flex;gap:8px;">
    <input name="q" type="text" placeholder="Search modules..." class="search-input" value="<?php echo isset($_GET['q']) ? htmlspecialchars($_GET['q']) : ''; ?>">
    <button type="submit" class="search-btn">Search</button>
    <?php if (isset($_GET['q']) && $_GET['q'] !== ''): ?>
      <a href="index.php" class="search-btn" style="text-decoration:none;display:inline-block;padding:0 16px;line-height:2.2;">Clear</a>
    <?php endif; ?>
    </form>
  </section>


  <!-- Modules Grid -->
  <main class="wrap grid">
    <!-- Example module card -->
    <!--
    <article class="card">
      <a href="modules/en-afristory/index.html" target="_blank" class="card-media">
        <img src="modules/en-afristory/af.png" alt="African Storybook" class="card-img">
      </a>
      <div class="card-body">
        <h3 class="card-title">
          <a href="modules/en-afristory/index.html" target="_blank">African Storybook Project</a>
        </h3>
        <p class="card-desc">Illustrated stories to help children learn to read, gathered from African communities.</p>
        <ul class="card-links">
          <li><a href="modules/en-afristory/firstwords.html" target="_blank">First Words</a></li>
          <li><a href="modules/en-afristory/firstsentences.html" target="_blank">First Sentences</a></li>
          <li><a href="modules/en-afristory/firstparagraphs.html" target="_blank">First Paragraphs</a></li>
        </ul>
      </div>
    </article>
    -->


  
  <?php
      $modcount = 0;

      $fsmods = getmods_fs();

      $searchQuery = isset($_GET['q']) ? trim($_GET['q']) : '';
      if ($searchQuery !== '') {
          $fsmods = array_filter($fsmods, function($mod) use ($searchQuery) {
              // Search in title and description (if available)
              $title = isset($mod['title']) ? $mod['title'] : '';
              $desc = isset($mod['desc']) ? $mod['desc'] : '';
              return stripos($title, $searchQuery) !== false || stripos($desc, $searchQuery) !== false;
          });
      }

      # if there were any modules found in the filesystem
      if ($fsmods) {

          # get a list from the databases (where the sorting
          # and visibility is stored)
          $dbmods = getmods_db();

          # populate the module list from the filesystem 
          # with the visibility/sorting info from the database
          foreach (array_keys($dbmods) as $moddir) {
              if (isset($fsmods[$moddir])) {
                  $fsmods[$moddir]['position'] = $dbmods[$moddir]['position'];
                  $fsmods[$moddir]['hidden'] = $dbmods[$moddir]['hidden'];
              }
          }

          # custom sorting function in common.php
          uasort($fsmods, 'bypos');

          # whether or not we were able to get anything
          # from the DB, we show what we found in the filesystem
          foreach (array_values($fsmods) as $mod) {
              if ($mod['hidden'] || !$mod['fragment']) { continue; }
              if ($mod['moddir'] === 'en-imathas') { continue; } // Skip en-imathas module

              $nonLinkedMods = array(
                'en-asst_medical',
                'en-causebooks',
                'en-ck12'
              );



              $dir  = $mod['dir'];
              $moddir  = $mod['moddir'];
              /////////////////////////////////////////////
              echo '<article class="card">';
              ob_start();
              include $mod['fragment'];
              $fragmentContent = ob_get_clean();
              $fragmentContent = str_replace('<ul>', '<ul class="card-links">', $fragmentContent);
              $fragmentContent = str_replace('wikipedia_en_all_maxi_2023-02/', 'en_wikipedia_for_schools_2013/A/index.htm', $fragmentContent);
              $fragmentContent = str_replace('<ul class="double">', '<ul class="card-links">', $fragmentContent);
              $fragmentContent = str_replace('<ul class=double>', '<ul class="card-links">', $fragmentContent);
              $fragmentContent = str_replace('<ul class="triple">', '<ul class="card-links">', $fragmentContent);
              $fragmentContent = str_replace('<ul class=triple>', '<ul class="card-links">', $fragmentContent);
              $fragmentContent = str_replace('<ul class="quad">', '<ul class="card-links">', $fragmentContent);
              $fragmentContent = str_replace('<ul class=quad>', '<ul class="card-links">', $fragmentContent);
              $fragmentContent = str_replace('<div class="indexmodule">', '<div class="card-body">', $fragmentContent);
              $fragmentContent = str_replace('<p>', '<p class="card-desc">', $fragmentContent);
              $fragmentContent = str_replace('<p class="kolibri-intro">', '<p class="card-desc">', $fragmentContent);
              $fragmentContent = str_replace('<p class="smallblurb">', '<p class="card-desc">', $fragmentContent);
              //$fragmentContent = str_replace('<a href="modules/', '<a target="_blank" class="card-media" href="modules/', $fragmentContent);
              $fragmentContent = str_replace('<h2>', '<h3 class="card-title">', $fragmentContent);

              $fragmentContent = preg_replace('/<ul class="card-links">.*?<\/ul>/is', '', $fragmentContent);//remove existing ul to avoid duplication
              $fragmentContent = preg_replace('/<ul\s+class=(["\'])double\1>.*?<\/ul>/is', '', $fragmentContent); // remove <ul class="double"> or <ul class='double'>
              $fragmentContent = preg_replace('/<ul\s+class=(["\'])triple\1>.*?<\/ul>/is', '', $fragmentContent); // remove <ul class="double"> or <ul class='double'>
              $fragmentContent = preg_replace('/<ul\s+class=(["\'])quad\1>.*?<\/ul>/is', '', $fragmentContent); // remove <ul class="double"> or <ul class='double'>

              $fragmentContent = preg_replace('/<p style="margin-left:\s*130px;">.*?<\/p>/is', '', $fragmentContent);
              $fragmentContent = preg_replace('/<div style="margin-left:\s*130px;">.*?<\/div>/is', '', $fragmentContent);
              $fragmentContent = preg_replace("/<p style='margin-left:\s*130px;'>.*?<\/p>/is", '', $fragmentContent);

              $fragmentContent = preg_replace('/<table.*?>.*?<\/table>/is', '', $fragmentContent);

              $fragmentContent = preg_replace_callback(
                  '/<p class="card-desc">(.*?)<\/p>/is',
                  function ($matches) {
                      $desc = trim($matches[1]);
                      // Split by sentence-ending punctuation followed by space or end of string
                      $sentences = preg_split('/(?<=[.!?])\s+/', $desc, -1, PREG_SPLIT_NO_EMPTY);
                      if (count($sentences) > 1) {
                          // Retain only the first sentence
                          return '<p class="card-desc">' . $sentences[0] . '</p>';
                      } else {
                          // Leave unchanged
                          return $matches[0];
                      }
                  },
                  $fragmentContent
              );

              $fragmentContent = preg_replace_callback(
                  '/<img\s+src="(modules\/en-iicba\/[^"]+)"([^>]*)>/i',
                  function ($matches) {
                      $imgTag = $matches[0];
                      $href = 'modules/en-iicba/';
                      return '<a href="' . $href . '" target="_blank">' . $imgTag . '</a>';
                  },
                  $fragmentContent
              );

              // Ensure only the first <p class="card-desc"> is kept
              $count = 0;
              $fragmentContent = preg_replace_callback(
                  '/<p class="card-desc">.*?<\/p>/is',
                  function ($matches) use (&$count) {
                      $count++;
                      return $count === 1 ? $matches[0] : '';
                  },
                  $fragmentContent
              );

              if (in_array($mod['moddir'], $nonLinkedMods)) {
                    // Wrap the first <img ...> with the module link
                    $fragmentContent = preg_replace(
                        '/(<img[^>]+>)/i',
                        '<a href="modules/' . $mod['moddir'] . '/" target="_blank">$1</a>',
                        $fragmentContent,
                        1 // Only the first image
                    );
              }


              $fragmentContent = preg_replace('/<[^>]*class="attribution"[^>]*>.*?<\/[^>]+>/is', '', $fragmentContent);

              echo $fragmentContent;


              echo "</article>";
              /////////////////////////////////////////////
              ++$modcount;
          }

      }

      if ($modcount == 0) {
          echo $lang['no_mods_error'];
      }

  ?>



    <!-- duplicate or generate more cards here -->
  </main>





  <!-- Footer -->
  <footer class="site-footer">
    <div class="wrap">© 2025 Global Hope. Powered by DreamCube.</div>
  </footer>

  <script>
    // small script to toggle nav on narrow screens
    document.querySelector('.nav-toggle').addEventListener('click', function () {
      document.querySelector('.main-nav').classList.toggle('open');
    });
  </script>

  <script>
  document.addEventListener("DOMContentLoaded", () => {
    const hero = document.querySelector(".hero-animated");
    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            hero.classList.add("play");
          }
        });
      },
      { threshold: 0.4 }
    );
    observer.observe(hero);
  });
  </script>
<script>
  document.querySelectorAll('.dropdown-toggle').forEach(function(toggle) {
    toggle.addEventListener('click', function(e) {
      e.preventDefault();
      // Close other open dropdowns
      document.querySelectorAll('.nav-dropdown.open').forEach(function(openDropdown) {
        if (openDropdown !== toggle.parentElement) {
          openDropdown.classList.remove('open');
        }
      });
      // Toggle current dropdown
      toggle.parentElement.classList.toggle('open');
    });
  });

  // Optional: close dropdown when clicking outside
  document.addEventListener('click', function(e) {
    if (!e.target.closest('.nav-dropdown')) {
      document.querySelectorAll('.nav-dropdown.open').forEach(function(openDropdown) {
        openDropdown.classList.remove('open');
      });
    }
  });
  </script>

</body>
</html>
