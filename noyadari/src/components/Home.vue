<template>
  <div>
    
    <div>
      <b-table :items="itemsArr">
      </b-table>
    </div>

    <b-button class="button is-clear" @click="addItem"> [+] New Sensor</b-button>

  </div>
</template>

<script>

export default {
  computed: {
    itemsArr: function() {
      return this.$store.getters.items ? 
        Object.values(this.$store.getters.items) : []
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
  mounted() {
    this.$store.dispatch('fetchItems')
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
