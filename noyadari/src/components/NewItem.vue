<template>
  <div>
    <center>
      <div>
         <b-field label="Scan QR">
                  <qrcode-reader @init="onInit" @decode="onDecode" :paused="paused"></qrcode-reader>    
          </b-field>
          <b-field label="Item Sn">
              <b-input v-model="newItem.sn" readonly required></b-input>
          </b-field>
          <b-field label="Item Name">
                  <b-input v-model="newItem.name"></b-input>
          </b-field>
          <button class="button is-primary" @click="addItem">ADD ITEM</button>&nbsp;
          <button class="button is-warning" @click="$router.go(-1)">Cancel</button>
    </div>
    </center>

  </div>
</template>

<script>

import { parseUrl } from '../util/query.js'

export default {
  data() {
    return {
      items: this.$store.getters.items
    }
  },
  methods: {
    addItem: function() {
      if (this.newItem.sn) {
        this.items.push(this.newItem);
        this.newItem = {};
        this.$router.push("home");
      } else {
        this.$toast.open({
          message: "Item SN is required",
          type: "is-danger"
        });
      }
    },
    onDecode: function(content) {
      var query = parseUrl(content);
      console.log(query);
      this.newItem.sn = query.sn;
      this.paused = true;
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
