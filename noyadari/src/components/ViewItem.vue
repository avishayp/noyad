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

      <line-chart
        title="open/close events" xtitle="time" ytitle="open/close"
        library="{ curve: false, pointSize: 0 }"
        :data="mockOcTimeSeries">
      </line-chart>

    </b-card>

  </div>


</template>

<script>

import { timeFormat } from '@/util/query'

export default {
  data() {
    return {
      mockOcTimeSeries: {
        '2018-09-01': 0,

        '2018-09-03T23:36:07.818Z': 0,
        '2018-09-03T23:36:07.819Z': 1,
        '2018-09-04T07:36:07.818Z': 1,
        '2018-09-04T07:36:07.819Z': 0,

        '2018-09-07T23:36:07.818Z': 0,
        '2018-09-07T23:36:07.819Z': 1,
        '2018-09-08T23:42:07.820Z': 1,
        '2018-09-08T23:42:07.821Z': 0,

        '2018-09-12T09:42:07.819Z': 0,
        '2018-09-12T09:42:07.820Z': 1,
        '2018-09-14T09:42:07.820Z': 1,
        '2018-09-14T09:42:07.822Z': 0,

        '2018-09-16': 0
      },
      items: {},
      fields: [
        { key: 'status', label: 'State' , formatter: s => s ? 'open' : 'close'},
        { key: 'ts', label: 'recorded at', formatter: d => timeFormat(d) }
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
