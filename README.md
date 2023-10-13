# descriptiongen: Automatically generate descriptions for paintings

<h2>How It Works</h3>
<p>First, the program gets the image(saved locally) called <code>image.png</code>, and prompts Google Bard to describe the image using it's image tools. This program uses the <code>bardapi</code> library, which allows you to prompt Bard for free.</p>

<h2>Installing <code>bardapi</code></h2>
<p>
  The following instructions are applicable only to Windows
  <ul>
    <li>Open a new terminal, and type <code>pip install bardapi</code></li>
    <li>To check that it installed, type <code>bardapi --version</code></li>
  </ul>
</p>

<h2>API Keys</h2>
<h3>Generating API Keys</h3>
<p>
  <ul>
    <li>Go to <code>bard.google.com</code></li>
    <li>Open the <code>Devtools/Application</code> tab</li>
    <li>Go to <code>Storage/Cookies/https://bard.google.com</code></li>
    <li>In the right panel, find <code>Secure 1-PSID</code></li>
    <li>Copy the value and paste it into the token parameter for the <code>Bard()</code> definition function</li>
  </ul>
</p>
<h3>If The API Key Doesn't Work</h4>
<p>
  <ul>
    <li>Clear Browsing History for All Time</li>
    <li>Repeat the instructions above</li>
    <li>If it still doesn't work, generate the API key for a new account</li>
  </ul>
</p>
<h2>How API Keys Work</h2>
<p>The API keys are unique for each user, and often every session. Therefore, they have to often be regenerated. Different accounts will require you to regenerate the API key and repeat all the steps above.</p>
