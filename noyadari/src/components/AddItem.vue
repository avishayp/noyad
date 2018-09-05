<template>
  <div>
    <center>
      <div class="a-centric">

        <h2>Scan QR code or enter sn</h2>
        <qrcode-reader @decode="onDecode" :paused="paused"></qrcode-reader>
        <b-form v-on:submit.prevent="addItem">
        <b-form-group label="Sensor SN:"
                      label-for="snInput"
                      class="b-lefty">
          <b-form-input id="snInput"
                        v-model="sn"
                        placeholder="Enter serial number...">
          </b-form-input>
        </b-form-group>

        <b-button type="submit" :disabled="!sn" variant="primary" class="b-lefty">Continue</b-button>
        <b-button type="cancel" @click="$router.go(-1)">Cancel</b-button>
        </b-form>
    </div>
    </center>

  </div>
</template>

<script>

import { parseUrl } from '../util/query.js'

export default {
  data() {
    return {
      sn: null,
      paused: false
    }
  },
  methods: {
    addItem: function() {
      let newItem = {
        sn: this.sn,
        name: "new sensor #" + Object.keys(this.$store.getters.items).length,
        details: '',
        updated: Date.now(),
        createBy: this.$store.getters.userName,
        count: 0,
        lat: 0,
        lng: 0
      }

      this.$store.dispatch('addItem', newItem)
      this.$router.push("/edit?sn=" + newItem.sn)
      this.sn = null
    },
    onDecode: function(content) {
      if (!content) return

      var query = parseUrl(content)
      console.log(query)
      this.sn = query.sn
      if (this.sn) {
        this.paused = true
        this.addItem()
      }
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
