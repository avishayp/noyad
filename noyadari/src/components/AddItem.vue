<template>
  <div class="hello">
    <nav class="navbar is-primary" style="width:100%" role="navigation" aria-label="dropdown navigation">
     <div class="navbar-brand">
            <a class="navbar-item">
                <img src="https://bulma.io/images/bulma-logo.png" alt="Buefy">
            </a>
      </div>
      <div class="navbar-end">
              <div class="logout" v-if="userLoggedIn == 1"> 
                 <button class="button is-danger" @click="logOut">LOG OUT</button>
              </div>     
      </div>
    </nav>
    <br>
    <center>
      <div style="width: 40%">
         <b-field label="Scan QR">
                  <qrcode-reader @init="onInit" @decode="onDecode" :paused="paused"></qrcode-reader>    
          </b-field>
          <b-field label="Item Sn">
              <b-input v-model="newItem.sn" readonly required></b-input>
          </b-field>
          <b-field label="Item Name">
                  <b-input v-model="newItem.name"></b-input>
          </b-field>
          <button class="button is-primary" @click="addItem">ADD ITEM</button>&nbsp;
          <button class="button is-warning" @click="$router.go(-1)">Cancel</button>
    </div>
    </center>

  </div>
</template>

<script>
"use strict";
import { db } from "../mixins/firebase.js";
import urlParser from "url-parse";
import queryString from "query-string";

let items = db.ref("items");

export default {
  name: "HelloWorld",
  props: {
    msg: String
  },
  data() {
    return {
      name: "fast",
      paused: false,
      errorMessage: "",
      newItem: {
        id: "",
        name: "",
        sn: "",
        email: localStorage.getItem("email")
      },
      username: null,
      userLoggedIn: null
    };
  },
  methods: {
    addItem: function() {
      if (this.newItem.sn) {
        items.push(this.newItem);
        this.newItem = {};
        this.$router.push({ name: "home" });
      } else {
        this.$toast.open({
          message: "Item Sn is required",
          type: "is-danger"
        });
      }
    },
    onDecode: function(content) {
      var url = new urlParser(content);
      var query = queryString.parse(url.query);
      console.log(query);
      this.newItem.sn = query.sn;
      this.paused = true;
    },
    onInit: function(promise) {
      promise
        .then(() => {
          console.log("Successfully initilized! Ready for scanning now!");
        })
        .catch(error => {
          if (error.name === "NotAllowedError") {
            this.errorMessage = "Need access to your camera";
          } else if (error.name === "NotFoundError") {
            this.errorMessage = "No camera on your device?";
          } else if (error.name === "NotSupportedError") {
            this.errorMessage =
              "Seems like this page is served in non-secure context (HTTPS, localhost or file://)";
          } else if (error.name === "NotReadableError") {
            this.errorMessage =
              "Couldn't access your camera. Is it already in use?";
          } else if (error.name === "OverconstrainedError") {
            this.errorMessage =
              "Constraints don't match any installed camera. Did you asked for the front camera although there is none?";
          } else {
            this.errorMessage = "UNKNOWN ERROR: " + error.message;
          }
        });
    },
    userinfo: function() {
      this.username = localStorage.getItem("username");
      this.userLoggedIn = localStorage.getItem("userLoggedIn");
    },
    logOut: function() {
      localStorage.clear();
      this.$router.push({ name: "login" });
    }
  },
  mounted() {
    this.userinfo();
    if (this.userLoggedIn == null) {
      this.$router.push({ name: "login" });
    }
  },
  components: {}
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
.logout {
  position: absolute;
  top: 10px;
  right: 20px;
}
</style>
