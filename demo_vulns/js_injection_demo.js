const express = require('express');
const app = express();

app.get('/run', (req, res) => {
  const cmd = req.query.cmd;
  require('child_process').exec(cmd); // Intentionally insecure
  res.send('ok');
});

app.listen(3000);
