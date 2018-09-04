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
    </nav><br>
    <button class="button is-clear" @click="gotoAddItem"> + ADD ITEM</button>
    <div>
      <table class="table" style="width : 100%;">
      <thead>
        <tr>
          <th style="text-align: center;">Item Sn</th>
          <th style="text-align: center;">Item Name</th>
          <th style="text-align: center;">Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(item,index) in items" :key="index">
          <td style="text-align: center;">{{item.sn}}</td>
          <td style="text-align: center;">{{item.name}}</td>
          <td style="text-align: center;">
            <button class="button is-clear is-small" @click="removeItem(item)">Delete</button>
            <button class="button is-clear is-small" @click="removeItem(item)">Edit</button>
            <button class="button is-clear is-small" @click="removeItem(item)">View</button>
          </td>
        </tr>
      </tbody>
    </table>
    </div>

  </div>
</template>

<script>
import { db } from "../mixins/firebase.js";

let items = db.ref("items");

export default {
  name: "HelloWorld",
  props: {
    msg: String
  },
  firebase: {
    items: items
  },
  data() {
    return {
      name: "fast",
      username: null,
      userLoggedIn: null
    };
  },
  methods: {
    removeItem: function(item) {
      items.child(item[".key"]).remove();
    },
    post: function() {
      console.log(this.name);
      this.$http
        .get("https://vue-project-9e30c.firebaseio.com/user.json")
        .then(data => {
          console.log(data);
        });
    },
    gotoAddItem: function() {
      this.$router.push({
        name: "additem"
      });
    },
    userinfo: function() {
      this.username = localStorage.getItem("username");
      this.userLoggedIn = localStorage.getItem("userLoggedIn");
    },
    logOut: function() {
      localStorage.clear();
      this.$router.push({name: 'login'});
    }
  },
  mounted() {
    this.userinfo();
    if (this.userLoggedIn == null) {
      this.$router.push({name: 'login'});
    }
  }
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
