<template>
  <div>
    
    <div>
      <b-table responsive flex striped hover
               :items="items"
               :fields="fields"
               @row-clicked="viewItem">

      <template slot="actions" slot-scope="row">
        <b-button size="sm" variant="success">
          details
        </b-button>
      </template>               
      </b-table>
    </div>

    <b-button variant="primary" @click="addItem"> [+] New Sensor</b-button>
    <i class="fa fa-android"></i>

  </div>
</template>

<script>
import { timeFormat } from '@/util/query'

export default {
  data() {
    return {
      fields: [
        { key: 'sn', label: 'Unit S.N' },
        { key: 'status', label: 'Status' , formatter: s => s ? 'disconnected' : 'connected' },
        { key: 'updated', label: 'Last connected', formatter: d => timeFormat(d) },
        { key: 'valve', label: 'Valve state', formatter: v => v ? 'open' : 'close' },
        { key: 'openLastDay', label: '#open last day', formatter: v => v || 3 },
        { key: 'openLastMonth', label: '#open last month', formatter: v => v || 42 },
        { key: 'totalOpened', label: 'total opening time', formatter: v => v || '100h' },
        { key: 'actions', label: '' }
      ],
      items: []
    }
  },
  methods: {
    viewItem(item) {
      this.$router.push('/view/?sn=' + item.sn)
    },
    addItem() {
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
