<template>
  <div>

    <b-button id="spaced" href="/home">&times; close</b-button>

    <b-card :title="'SN: ' + item.sn"
            :sub-title="'name:' + item.name">

      <p class="card-text">{{item.details}}</p>

      <b-table responsive flex striped hover
               :items="ocEvents"
               :fields="fields">              
      </b-table>
    </b-card>

  </div>
</template>

<script>

export default {
  data() {
    return {
      items: {},
      fields: [
        { key: 'status', label: 'State' , formatter: s => s ? 'open' : 'close'},
        { key: 'ts', label: 'recorded at', formatter: d => d ? new Date(d).toISOString() : '' }
      ]
    }
  },
  computed: {
    item() {
      return this.items[this.$router.currentRoute.query.sn] || {}
    },
    ocEvents() {
      return [
        {state: false, ts: 1536273367820},
        {state: true, ts: 1536274367820},
        {state: false, ts: 1536275367820}
      ]
    }
  },
  firebase() {
    return {
      items: {
        source: this.$store.getters.itemsRef,
        asObject: true
      }
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  #spaced {
    margin-top: 10px;
    margin-bottom: 10px
  }
</style>
