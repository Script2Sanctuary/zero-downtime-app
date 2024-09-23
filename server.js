const express = require('express');
const app = express();
const port = process.env.PORT || 3000;

// app.get('/', (req, res) => {
//   res.send('Hello from Kubernetes with Zero Downtime Deployment!');
// });

// app.get('/', (req, res) => {
//   res.send('Updated: Hello from Kubernetes with Zero Downtime Deployment (v2)!');
// });

app.get('/', (req, res) => {
  res.send('Updated: Hello from Kubernetes with Downtime (v3)!');
});


app.listen(port, () => {
  console.log(`App listening on port ${port}`);
});
