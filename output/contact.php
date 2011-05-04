<?php
$shitlist = array(
    '203.247.145.10',
    '220.226.63.254',
    '198.133.178.133',
    '206.204.190.33',
    '72.232.228.106',
    '72.237.17.120',
    '93.157.169.18',
);
if ((array_key_exists('REMOTE_ADDR', $_SERVER) && in_array($_SERVER['REMOTE_ADDR'], $shitlist)) ||
    (array_key_exists('HTTP_X_FORWARDED_FOR', $_SERVER) && in_array($_SERVER['HTTP_X_FORWARDED_FOR'], $shitlist)) ||
    (array_key_exists('blogurl', $_POST) && preg_match('/(casino|adult|viagra|cialis|valium|lorazepam|tramadol|phentermine|ringtone)/i',$_POST['blogurl'])) ||
    (array_key_exists('email', $_POST) && preg_match('/goldfish?ka/i',$_POST['email'])) ||
    (array_key_exists('comments', $_POST) && preg_match('/<a href=\\\?["\']?\s*https?:/i', $_POST['comments'])) ||
    (!empty($_POST['blogurl']) && ($_POST['blogurl'] === $_POST['feedurl'])))
{
    die("Spamming is a sin. You won't enjoy your dirty money.\n");
}
if (isset($_SERVER['force_no_vary']) &&
    isset($_SERVER['nokeepalive']) &&
    isset($_SERVER['ssl_unclean_shutdown']))
{
    die("You think I'm stupid, bitch?\n");
}
ini_set("display_errors", "Off");
header("Content-type: text/html; charset=utf-8");
echo '<?xml version="1.0"?>';
?>
<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
  <title>Planet Terasi: Contact</title>
  <meta name="description" content="Planet Terasi is an aggregate blog about technology in general with a preference for original Indonesian-related technology content.">
  <meta name="author" content="Ronny Haryanto">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="icon" href="images/favicon.png">
  <link rel="apple-touch-icon" href="images/apple-touch-icon.png">
  <link rel="alternate" href="/rss20.xml">
  <link rel="stylesheet" href="terasi.css">
  <link rel="stylesheet" media="handheld" href="handheld.css">
  <script src="http://ajax.cdnjs.com/ajax/libs/modernizr/1.7/modernizr-1.7.min.js"></script>
  <script type="text/javascript" src="http://use.typekit.com/isv0gey.js"></script>
  <script type="text/javascript">try{Typekit.load();}catch(e){}</script>
</head>
<body>
<a name="top"></a>
<section id="page">
  <header>
    <div class="wrap">
      <h1 id="title"><a href="http://planet.terasi.net">Planet Terasi</a></h1>
      <h2 id="tagline">Think.&nbsp;Read.&nbsp;Write.</h2>

      <nav>
        <ul>
          <li class="about"><a href="#about">About</a></li>
          <li class="contributors"><a href="#contributors">Contributors</a></li>
          <li class="contact"><a href="contact.php">Contact</a></li>
        </ul>
      </nav>
    </div>
  </header>
  <section id="main">
    <section id="contact">
      <header>
        <h1>Contact Planet Terasi's Maintainer</h1>
      </header>

      <p>NOTES/FAQ:
      <ul>
      <li>I can't guarantee when or if I will add/remove your blog or respond to
      your inquiry. I usually review suggestions about once a month. More urgent
      inquiries usually get quicker response from me.</li> 
      <li>There are no fixed criteria for inclusion in Planet Terasi, in general
      as long as your blog is in line with Planet Terasi's general theme
      (technology with <strong>preference</strong> for original Indonesian-related
       contents), then I will most likely add it. If it's
      not really in line with Planet Terasi's topics/themes but you think it
      should be added, let me know anyway and explain in the comments your reasons.</li>
      <li>I will NOT add blogs that are: specifically designed/written to increase its own traffic, splogs
      (spam blogs), mostly SEO stuff, mainly personal posts, religious, political, mainly tutorials,
      highly technical content (e.g. lots of source code). Discussions on <strong>why</strong>
      something is/should (not) be done is much more interesting than <strong>how</strong> to do
      something.</li>
      <li>If you don't want to syndicate every content on your blog in Planet
      Terasi, then you can dedicate a particular category/tag for your posts that are
      going to be included in Planet Terasi. This will work as long as there is a
      feed specific to that particular category/tag. Use that feed URL as the blog
      URL above when suggesting.</li>
      </ul></p>

      <p>Thanks,<br/>Ronny</p>

      <?php if ($_POST['submitted'] == 'yes'): ?>
      <?php
      $body = "Planet Terasi Feedback\n\n";
      $body .= "About: " . $_POST['about'] . "\n";
      $body .= "From: " . $_POST['name'] . " <" . $_POST['email'] . ">\n";
      $body .= "Blog URL: " . $_POST['blogurl'] . "\n";
      $body .= "Feed URL: " . $_POST['feedurl'] . "\n";
      $body .= "Comments:\n". $_POST['comments']."\n\n------\n\n";

      $body .= "SERVER variables:\n";
      foreach($_SERVER as $key => $val)
      {
          $body .= "$key:\t\t\t$val\n";
      }

      if (mail("ronny@haryan.to", "Planet Terasi Feedback", $body))
      {
          echo "<p>Message has been sent. Thanks.</p>";
      }
      else
      {
          echo "<p>Message was NOT sent. Sorry. Please try again later.</p>";
      }

      ?>
      <?php else: ?>

      <form method="POST" name="frm" id="frm">
      <input type="hidden" name="submitted" value="yes" />

      <p><span class="q">What is it about?</span><br />
      <select size="1" name="about" id="about">
      <option value="add">I want to suggest a site to be added to Planet Terasi</option>
      <option value="remove">I want to suggest a site to be removed from Planet Terasi</option>
      <option value="change">I want to change my blog's URL, name, etc.</option>
      <option value="error">Something in Planet Terasi is not working properly</option>
      <option value="general">I have a general suggestion regarding Planet Terasi</option>
      <option value="question">I have a question regarding Planet Terasi</option>
      <option value="feedback">I would like to give a feedback (praise, constructive criticism)</option>
      </select></p>

      <p><span class="q">Your name:</span><br />
      <input type="text" name="name" id="name" size="40"
          value="<?php echo htmlentities($_POST['name']);?>" /></p>

      <p><span class="q">Your email address:</span><br />
      <input type="text" name="email" id="email" size="40"
          value="<?php echo htmlentities($_POST['email']);?>" /></p>

      <p><span class="q">The URL of the blog:</span><br />
      <input type="text" name="blogurl" id="blogurl" size="60"
          value="<?php echo htmlentities($_POST['blogurl']);?>" /></p>

      <p><span class="q">The URL of the RSS/Atom feed of the blog:</span><br />
      <input type="text" name="feedurl" id="feedurl" size="60"
          value="<?php echo htmlentities($_POST['feedurl']);?>" /></p>

      <p><span class="q">Comments or reasons:</span><br />
      <textarea rows="5" cols="60" id="comments" name="comments"><?php
          echo htmlentities($_POST['comments']);?></textarea></p>

      <p><input type="submit" value="Submit" /></p>
      </form>

      <?php endif; ?>

      <p><a href="http://planet.terasi.net/">Go Back To Planet Terasi</a></p>
    </section>

  </section>

  <footer>
    <section id="about">
      <header>
        <a name="about"></a>
        <h2>About Planet Terasi</h2>
      </header>

      <p>Planet Terasi is an aggregate blog about <em>technology</em> in general with a preference for original
      <em>Indonesian-related technology content</em>. Occasionally it may include other non-technology posts that are
      still Indonesian-related. Personal posts may creep in once in a while (blogs are personal by nature after all),
      but contributors are generally encouraged to either keep personal posts to a minimum, or provide a specific feed
      (e.g. by tag) for Planet Terasi. Planet Terasi may contain articles in Bahasa Indonesia and in English.</p>

      <p>Planet Terasi is maintained by <a
      href="http://ronny.haryan.to">Ronny&nbsp;Haryanto</a>.
      </p>

      <p>Planet Terasi is updated every hour and was most recently
      updated at <time datetime="2011-03-27T00:47:29+00:00">27 Mar 2011 12:47 AM <abbr
      title="Coordinated Universal Time (GMT)">UTC</abbr></time>.</p>

      <a href="#top" class="top">&uarr;</a>
    </section>

    <section id="disclaimers">
      <header>
        <h2>Disclaimers</h2>
      </header>

      <p>All blog posts are the personal views of the
      contributors and do not necessarily reflect Planet Terasi and its
      maintainer's views. Planet Terasi and its maintainer may not be
      held responsible for the contents of the contributors' individual
      blogs. Please consult the individual blogs for licensing and
      copyright information.</p>

      <a href="#top" class="top">&uarr;</a>
    </section>

    <section id="syndications">
      <header>
        <h2>Syndications</h2>
      </header>

      <ul>
        <li><a href="rss20.xml">RSS 2.0</a></li>
        <li><a href="rss10.xml">RSS 1.0</a></li>
        <li><a href="opml.xml">OPML</a></li>
        <li><a href="foafroll.xml">FOAF</a></li>
      </ul>

      <a href="#top" class="top">&uarr;</a>
    </section>

    <section id="contributors">
      <a name="contributors"></a>
      <header>
        <h2>Contributors</h2>
      </header>

      <ul>
          <li class="contributor"><a href="http://sarapanekonomi.blogspot.com/" title="'Sarapan Ekonomi,">'Sarapan Ekonomi,</a></li>
          <li class="contributor"><a href="http://affanzbasalamah.wordpress.com" title="Admin Juga Manusia 2.0 (tm) » Computer &amp; Networks">Affan Basalamah</a></li>
          <li class="contributor"><a href="http://agusset.blogspot.com/" title="my opinion">Agus Setiawan</a></li>
          <li class="contributor"><a href="http://doeljoni.blogsome.com" title="Scrapyard of mine">Ahmad SS Ramadhana</a></li>
          <li class="contributor"><a href="http://akuinginhijau.org" title="Aku Ingin Hijau">Aku Ingin Hijau</a></li>
          <li class="contributor"><a href="http://alexbudiyanto.web.id" title="AlexBudiyanto.Web.ID">Alex Budiyanto</a></li>
          <li class="contributor"><a href="http://andika-lives-here.blogspot.com/" title="Why Blog?">Andika Triwidada</a></li>
          <li class="contributor"><a href="http://andry.blogdetik.com" title="Andry S Huzain">Andry S Huzain</a></li>
          <li class="contributor"><a href="http://lazuardi.blogsome.com" title="YaLB">Ardian Lazuardi</a></li>
          <li class="contributor"><a href="http://aris.pituruh.com" title="Aris Priyantoro in the Cyber">Aris Priyantoro</a></li>
          <li class="contributor"><a href="http://ariya.blogspot.com/" title="don't code today what you can't debug tomorrow">Ariya Hidayat</a></li>
          <li class="contributor"><a href="http://layangan.com/asfik/blog" title="Asfihani">Asfihani</a></li>
          <li class="contributor"><a href="http://aulia.posterous.com" title="Loading Bars">Aulia Masna</a></li>
          <li class="contributor"><a href="http://bennychandra.com" title="BennyChandra.com">Benny Chandra</a></li>
          <li class="contributor"><a href="http://home.avianto.com/" title="life's like this - avianto's journal">Boy Avianto</a></li>
          <li class="contributor"><a href="http://budiputra.com" title="BudiPutra.com">Budi Putra</a></li>
          <li class="contributor"><a href="http://rahard.wordpress.com" title="Padepokan Budi Rahardjo » Teknologi Informasi">Budi Rahardjo</a></li>
          <li class="contributor"><a href="http://gadget.rootbox.or.id" title="Gadget and Stuff">Budiwijaya</a></li>
          <li class="contributor"><a href="http://ngadimin.org" title="Cecep Mahbub">Cecep Mahbub</a></li>
          <li class="contributor"><a href="http://dailysocial.net" title="DailySocial">DailySocial</a></li>
          <li class="contributor"><a href="http://denny.klorofil.org" title="The Denny Depok">Denny</a></li>
          <li class="contributor"><a href="http://didats.net" title="Didats Triadi » Technology">Didats Triadi</a></li>
          <li class="contributor"><a href="http://dgk.or.id" title="#!/Dudi/Gurnadi » Teknoblogia">Dudi Gurnadi</a></li>
          <li class="contributor"><a href="http://ryosaeba.wordpress.com" title="things left unsaid">Eko Juniarto</a></li>
          <li class="contributor"><a href="http://maseko.com" title="maseko's weblog">Eko Pramuyanto</a></li>
          <li class="contributor"><a href="http://enda.goblogmedia.com/" title="Enda Nasution's Weblog">Enda Nasution</a></li>
          <li class="contributor"><a href="http://firmanfirdaus.com" title="Firman Firdaus">Firman Firdaus</a></li>
          <li class="contributor"><a href="http://www.gajeto.com" title="Gajeto">Gajeto</a></li>
          <li class="contributor"><a href="http://hakitree.posterous.com" title="hakitree">HAKItree</a></li>
          <li class="contributor"><a href="" title="">Hardjono</a></li>
          <li class="contributor"><a href="http://harry.sufehmi.com" title="harry.sufehmi.com » Teknoblogia">Harry Sufehmi</a></li>
          <li class="contributor"><a href="http://www.hendyirawan.com" title="Hendy Irawan on Small Business Ideas">Hendy Irawan</a></li>
          <li class="contributor"><a href="http://idban.wordpress.com" title="!secandri's Blog">Idban Secandri</a></li>
          <li class="contributor"><a href="http://direktif.web.id" title="#direktif">Ikhlasul Amal</a></li>
          <li class="contributor"><a href="http://ip.sg.or.id" title=".. Minda Indra ..">Indra Pramana</a></li>
          <li class="contributor"><a href="http://irwinday.web.id" title="iWin Notes">Irwin Day</a></li>
          <li class="contributor"><a href="http://tayuang.blogspot.com/" title="iWin Notes">Irwin Day</a></li>
          <li class="contributor"><a href="http://www.itpin.com/blog" title="It Pin Arifin">It Pin</a></li>
          <li class="contributor"><a href="http://ivanlanin.wordpress.com" title="nan tak (kalah) penting">Ivan Lanin</a></li>
          <li class="contributor"><a href="http://julius.sirait.net/" title="Small Things on Small Screen">Julius Sirait</a></li>
          <li class="contributor"><a href="http://kyantonius.com" title="{Kemas Antonius}">Kemas Yunus Antonius</a></li>
          <li class="contributor"><a href="http://kyantonius.com" title="{Kemas Antonius}">Kemas Yunus Antonius</a></li>
          <li class="contributor"><a href="http://khairulu.blogsome.com" title="Inspirasi Pagi">Khairul Ummah</a></li>
          <li class="contributor"><a href="http://kuncoro.wordpress.com" title="Wara Wara">Kuncoro Wastuwibowo</a></li>
          <li class="contributor"><a href="http://kun.co.ro" title="Kuncoro++">Kuncoro Wastuwibowo</a></li>
          <li class="contributor"><a href="http://loopingterus.blogspot.com/" title="Looping Terus">Looping Terus</a></li>
          <li class="contributor"><a href="http://vavai.com" title="Migrasi Windows Linux » planet-terasi-aggregator">Masim Vavai Sugianto</a></li>
          <li class="contributor"><a href="" title="">Merdeka Blog</a></li>
          <li class="contributor"><a href="http://mrofiq.blogspot.com/" title="rofiq's blog">Muhammad Rofiq</a></li>
          <li class="contributor"><a href="http://takdir.blogspot.com/" title="Semangat Baru">Muhammad Takdir</a></li>
          <li class="contributor"><a href="http://suryana.or.id" title="suryana.or.id » Planet Terasi">Nana Suryana</a></li>
          <li class="contributor"><a href="http://satukubik.com" title="satukubik">Nanda Firdausi</a></li>
          <li class="contributor"><a href="http://www.navinot.com" title="NavinoT">Navinot</a></li>
          <li class="contributor"><a href="http://nurulwibawacahya.blogspot.com/" title=":: Just My Opinion ::">Nurul Wibawa Cahya</a></li>
          <li class="contributor"><a href="http://okto.silaban.net" title="Okto SiLaban">Okto Silaban</a></li>
          <li class="contributor"><a href="http://blogombal.org" title="blogombal">Paman Tyo</a></li>
          <li class="contributor"><a href="http://pipit.wordpress.com" title="Pipit's Blog @ Wordpress.com">Pipit</a></li>
          <li class="contributor"><a href="http://priyadi.net" title="Priyadi's Place">Priyadi Iman Nurcahyo</a></li>
          <li class="contributor"><a href="http://jalansutera.com" title="JalanSutera.com™">Pujiono</a></li>
          <li class="contributor"><a href="http://solyaris.wordpress.com" title="solaris">Rendy Anthony</a></li>
          <li class="contributor"><a href="http://www.rendymaulana.com" title="Rendy Maulana dot Com">Rendy Maulana</a></li>
          <li class="contributor"><a href="" title="">Reza Muhammad</a></li>
          <li class="contributor"><a href="http://romisatriawahono.net" title="RomiSatriaWahono.Net">Romi Satria Wahono</a></li>
          <li class="contributor"><a href="http://ronny.haryan.to/" title="Ronny Haryanto">Ronny Haryanto</a></li>
          <li class="contributor"><a href="http://steven.blogs.masterweb.net" title="Steven Haryanto">Steven Haryanto</a></li>
          <li class="contributor"><a href="http://www.temanmacet.com" title="Teman Macet (default)">Teman Macet</a></li>
          <li class="contributor"><a href="http://orangescale.net" title="Orangescale.NET">Thomas Arie Setiawan</a></li>
          <li class="contributor"><a href="http://id.wahyu.com" title="Wahyu Wijanarko">Wahyu Wijanarko</a></li>
          <li class="contributor"><a href="http://wpram.com/" title="William Computer Blog">William Pramana</a></li>
          <li class="contributor"><a href="http://wiryanto.wordpress.com" title="The works of Wiryanto Dewobroto">Wiryanto Dewobroto</a></li>
          <li class="contributor"><a href="http://yahyakurniawan.net" title="Blog Oom Yahya">Yahya Kurniawan</a></li>
          <li class="contributor"><a href="http://yulian.firdaus.or.id" title="Jay adalah Yulian">Yulian F. Hendriyana</a></li>
          <li class="contributor"><a href="http://blogindonesia.wordpress.com" title="Indonesian Best Blogs Directory">blogindonesia</a></li>
          <li class="contributor"><a href="http://gobzip.blogsome.com" title="weblog go bZip">gobzip</a></li>
      </ul>

      <div class="clearfix"></div>
      <a href="#top" class="top">&uarr;</a>
    </section>

    <div class="clearfix"></div>
  </footer>
</section>

<script src="//ajax.googleapis.com/ajax/libs/jquery/1.5.1/jquery.min.js"></script>
<script>window.jQuery || document.write('<script src="jquery-1.5.1.min.js">\x3C/script>')</script>
<script src="jquery.timeago.js"></script>
<script src="jquery.isotope.min.js"></script>
<script>
  var _gaq=[['_setAccount','UA-5657485-1'],['_trackPageview']];
  (function(d,t){var g=d.createElement(t),s=d.getElementsByTagName(t)[0];g.async=1;
  g.src=('https:'==location.protocol?'//ssl':'//www')+'.google-analytics.com/ga.js';
  s.parentNode.insertBefore(g,s)}(document,'script'));
  $("time").timeago();
  $("#page #main").isotope({
    itemSelector: 'article',
    layoutMode: 'masonry'
  });
  var _n = 0;
  $(window).bind('scroll', function(){
    _n += 1;
    if (_n < 200 && _n % 10 == 0) {
      $("#page #main").isotope('reLayout');
    }
  });
</script>
</body>
</html>
