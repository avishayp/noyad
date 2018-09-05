<template>
  <div>
    <center>
      <div class="a-centric">
        <h2>SN: {{item.sn}}</h2>
        <b-form v-on:submit.prevent="editItem">
        <b-form-group label="Name:"
                      class="b-lefty">
          <b-form-input v-model="item.name"
                        placeholder="Sensor name...">
          </b-form-input>
        </b-form-group>

        <b-form-group label="Details:"
                      class="b-lefty">
          <b-form-input v-model="item.details"
                        placeholder="Sensor details...">
          </b-form-input>
        </b-form-group>

        <b-button type="submit" :disabled="!item.name" variant="primary" class="b-lefty">Continue</b-button>
        <b-button type="cancel" @click="$router.go(-1)">Cancel</b-button>
        </b-form>
    </div>
    </center>

  </div>
</template>

<script>

export default {
  data() {
    return {
      item: {}
    }
  },
  methods: {
    editItem: function() {
      this.$store.dispatch('editItem', this.item)
      this.$router.push("/home")
      this.item = {}
    }
  },
  mounted() {
    let sn = this.$router.currentRoute.query.sn
    this.item = this.$store.getters.items[sn] || {}
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
