<template>
  <div>
    
    <div>
      <b-table :items="items">
      </b-table>
    </div>

    <b-button class="button is-clear" @click="addItem"> [+] New Sensor</b-button>

  </div>
</template>

<script>

export default {
  data() {
    return {
      items: {}
    }
  },
  methods: {
    viewItem: function() {
      // tbd
    },
    addItem: function() {
      this.$router.push('/add')
    }
  },
  firebase() {
    return {
      items: this.$store.getters.itemsRef
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
