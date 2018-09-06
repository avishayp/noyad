<template>
  <main id="app" class="section">
    <div class="container">
      <Header />
      <router-view></router-view>
    </div>
  </main>
</template>

<script>
import Header from './components/Header'

export default {
  components: {
    Header
  },
  methods: {
  },
  created() {
  }
};
</script>

<style>
body {
  font-family: "Roboto", sans-serif;
}

.b-lefty {
  text-align: left;
  margin: 10%
}

.a-centric {
  width: 80%
}

.blueish {
  background: lightblue
}
</style>
