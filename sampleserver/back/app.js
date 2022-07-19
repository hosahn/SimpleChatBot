const express = require("express");
const cors = require("cors");
const app = express();
const bodyPaser = require("body-parser");
const axios = require("axios");
const helmet = require("helmet");

app.use(helmet());
app.use(cors());
app.use(bodyPaser.json());
app.post("/message", async (req, res) => {
  try {
    const message = req.body.info || "Null";
    if (message == "Null") {
      res.send("메세지를 정확히 입력해주세요!");
    } else {
      const result = await axios.post("http://localhost:5000", {
        info: message,
      });
      res.send(result.data);
    }
  } catch (e) {
    res.send(e);
  }
});

app.listen(8080, () => {
  console.log("App Started");
});
