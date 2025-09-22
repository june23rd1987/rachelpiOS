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
      <h1 class="brand">Global Hope</h1>
      <nav class="main-nav">
        <a href="index.php"><?php echo strtoupper($lang['home']) ?></a>
        <a href="about.html"><?php echo strtoupper($lang['about']) ?></a>
        <?php
        echo "<a href=\"http://$_SERVER[SERVER_ADDR]:81/\" target=\"_blank\">KIWIX</a>";
        echo "<a href=\"http://$_SERVER[SERVER_ADDR]:8080/en/learn/#/home/\" target=\"_blank\">KOLIBRI</a>";
        ?>
        <a href="admin/modules.php" class="admin-link"><?php echo $lang['admin'] ?></a>
      </nav>
      <button class="nav-toggle" aria-hidden="true">☰</button>
    </div>
  </header>

  <!-- Hero -->
  <section class="hero">
    <div class="wrap hero-inner">
      <h2 class="hero-title">Explore Knowledge, Anytime, Offline</h2>
      <p class="hero-sub">A collection of educational resources accessible without internet.</p>
    </div>
  </section>

  <!-- Search -->
  <section class="wrap section">
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
              $dir  = $mod['dir'];
              $moddir  = $mod['moddir'];
              /////////////////////////////////////////////
              echo '<article class="card">';
              ob_start();
              include $mod['fragment'];
              $fragmentContent = ob_get_clean();
              $fragmentContent = str_replace('<ul>', '<ul class="card-links">', $fragmentContent);
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
</body>
</html>
