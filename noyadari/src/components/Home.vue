<template>
  <div>
    
    <div>
      <b-table :items="items" :fields="fields">
      </b-table>
    </div>

    <b-button class="button is-clear" @click="addItem"> [+] New Sensor</b-button>

  </div>
</template>

<script>

export default {
  data() {
    return {
      fields: [
        { key: 'sn', label: 'serial number' },
        { key: 'name' },
        { key: 'count' },
        { key: 'updated', label: 'last update', formatter: d => new Date(d).toISOString() }
      ],
      items: []
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
