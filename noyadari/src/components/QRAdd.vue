<template>
</template>

<script>

export default {
  methods: {
    addNewItem: function(sn) {
      let newItem = {
        sn: sn,
        name: "new sensor",
        details: '',
        updated: Date.now(),
        createBy: this.$store.getters.userName,
        count: 0,
        lat: 0,
        lng: 0
      }

      this.$store.commit('updateItem', newItem)
      this.$router.replace("/edit/?sn=" + newItem.sn)
    },
  },
  mounted() {
    console.log('qradd mounted')
    let sn = this.$router.currentRoute.query.sn
    if (!sn) {
      console.log('route requires sn param')
      this.$router.replace('/home')
      return
    }
    
    // if item exists - we go home
    this.$store.getters.itemsRef.child(sn)
    .once('value', snapshot => {
      if (snapshot.val()) {
        console.log(sn, 'already exists')
        this.$router.replace("/view/?sn=" + sn)
      } else {
        console.log(sn, 'not found')
        this.addNewItem(sn)
      }
    })
  }
};
</script>