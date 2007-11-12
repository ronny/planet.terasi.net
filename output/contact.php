<?php
$shitlist = array(
    '203.247.145.10',
    '220.226.63.254',
    '198.133.178.133',
    '206.204.190.33',
    '72.232.228.106',
    '72.237.17.120',
);
if (in_array($_SERVER['REMOTE_ADDR'], $shitlist) ||
    in_array($_SERVER['HTTP_X_FORWARDED_FOR'], $shitlist) ||
    preg_match('/(casino|adult|viagra|cialis|valium|lorazepam|tramadol|phentermine|ringtone)/i',$_POST['blogurl']) ||
    preg_match('/<a href=\\\?["\']?\s*https?:/i', $_POST['comments']) ||
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
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
    "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">

<head>
<title>Contact Planet Terasi's Maintainer</title>
</head>

<body>
<h1>Contact Planet Terasi's Maintainer</h1>

<p>NOTES/FAQ:
<ul>
<li>I can't guarantee when or if I will add/remove your blog or respond to
your inquiry. I usually review suggestions about once a month. More urgent
inquiries usually get quicker response from me.</li> 
<li>There are no fixed criteria for inclusion in Planet Terasi, in general
as long as your blog is in line with Planet Terasi's general theme
(technology and blogging with preference for original Indonesian-related
 contents), then I will most likely add it. If it's
not really in line with Planet Terasi's topics/themes but you think it
should be added, let me know anyway and explain in the comments your reasons.</li>
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

</body>

</html>
