<template>
  <div>
    <div style="background-color: grey;"><center>Login</center></div><br>
    <center>
            <div style="width :  40%">
                <b-field label="Email">
                    <b-input type="email" v-model="email"
                                    value="john@"
                                    maxlength="30"
                                    required>
                    </b-input>
                </b-field>
                <b-field label="Password">
                    <b-input type="password"
                        v-model="password"
                        @keyup.enter.native="login"
                        password-reveal
                        required >
                    </b-input>
                </b-field>
                <button class="button is-primary" @click="login">Login</button>
            </div>
    </center>
    
  </div>
</template>

<script>
export default {
  name: "HelloWorld",
  props: {
    msg: String
  },
  data() {
    return {
      name: "fast",
      email: null,
      password: null,
      user: {}
    };
  },
  methods: {
    login: function() {
      console.log(this.email, this.password);
      if (this.email && this.password) {
        this.$http
          .get("https://vue-project-9e30c.firebaseio.com/user.json")
          .then(data => {
            return data.json();
          })
          .then(data => {
            for (let key in data) {
              console.log(data[key]);
              this.user = data[key];
            }
            if (
              this.user.email == this.email &&
              this.user.password == this.password
            ) {
              this.$router.push({ name: "home" });
              localStorage.setItem("username", "test");
              localStorage.setItem("userLoggedIn", 1);
              localStorage.setItem("email",this.user.email);
              this.email = null;
              this.password = null;
            } else {
              this.$toast.open({
                message: "Invalid Username or password!",
                type: "is-danger"
              });
              this.email = null;
              this.password = null;
            }
          });
      } else {
        this.$toast.open({
          message: "Fill out Username or password!",
          type: "is-danger"
        });
      }
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
</style>
