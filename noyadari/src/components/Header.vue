<template>
<div>
  <b-navbar toggleable="md" type="light" variant="light">

    <b-navbar-brand href="#">
      <img src="@/assets/logo.png" height=60px/>
    </b-navbar-brand>

    <b-collapse v-if="user" is-nav id="nav_collapse">
      <b-navbar-nav class="ml-auto">
        <b-nav-item right>
          <p>user: {{user}}</p>
        </b-nav-item >
        
        <b-nav-item right>
          <b-button @click="logout">Sign out</b-button>
        </b-nav-item>
      </b-navbar-nav>
    </b-collapse>

  </b-navbar>
  </div>
</template>

<script>
export default {
  computed: {
    user() {
      return this.$store.getters.userName;
    }
  },
  methods: {
    logout: function() {
      this.$store.dispatch('logout')
      .then( () => { this.$router.push('/login') })
      .catch( err => {
        console.error('this should not happen', err.message)
        this.$router.push('/login')
      })
    }
  }
}
</script>