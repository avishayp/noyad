<template>
<div>
  <center>
    <div class="a-centric">

    <div v-if="attempts" class="b-lefty">
      <div v-if="userName" class="alert alert-success">
        <strong>Welcome {{userName}}</strong>
      </div>
      <div v-else class="alert alert-danger">
        <strong>Wrong email or password</strong>
      </div>
    </div>
    <div v-else class="b-lefty">
      <div class="alert alert-info">
        <strong>Login Details</strong>
      </div>
    </div>

    <b-form v-on:submit.prevent="login">
      <b-form-group label="Email:"
                    label-for="emailInput"
                    class="b-lefty">
        <b-form-input id="emailInput"
                      type="email"
                      v-model="user.email"
                      required
                      autocomplete="email"
                      placeholder="Your email...">
        </b-form-input>
      </b-form-group>
      <b-form-group label="Password:"
                    label-for="passwordInput"
                    class="b-lefty">
        <b-form-input id="passwordInput"
                      type="password"
                      autocomplete="current-password"
                      v-model="user.password"
                      required
                      placeholder="Your password...">
        </b-form-input>
      </b-form-group>
      <b-button type="submit" variant="primary" class="b-lefty">Submit</b-button>
    </b-form>
    </div>
  </center>
</div>
</template>

<script>

export default {
  data() {
    return {
      attempts: 0,
      user: {
        email: null,
        password: null
      }
    }
  },
  computed: {
      userName: function() {
        return this.$store.getters.userName
      }
  },
  methods: {
    login: function() {
      this.$store.dispatch('login', this.user)
        .then( () => {
          this.$router.go(-1)
        })
        .catch( err => {
          console.log('login failed for', this.user.email, err.message)
          this.attempts += 1
        })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
