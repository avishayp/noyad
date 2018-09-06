import Vue from 'vue';
import Vuex from 'vuex';
import Firebase from 'firebase';

const config = {
  apiKey: "AIzaSyBH4iNpikkJxR1PGNU-gS4yymaBTy9p2jM",
  authDomain: "noyad-ari.firebaseapp.com",
  databaseURL: "https://noyad-ari.firebaseio.com",
  projectId: "noyad-ari",
  storageBucket: "noyad-ari.appspot.com",
  messagingSenderId: "345943655765"
};

// Initialize Firebase
Firebase.initializeApp(config);

Vue.use(Vuex);

const store = new Vuex.Store({

  state: {
    user: null,
    items: Firebase.database().ref('items')
  },

  getters: {
    userName: state => state.user && state.user.split('@')[0],
    itemsRef: state => state.items
  },

  mutations: {
    waitUser: (state, callback) => {
      Firebase.auth().onAuthStateChanged( user => {
        state.user = user && user.email
        callback()
      })
    },
    setUser: state => {
      let user = Firebase.auth().currentUser
      state.user = user && user.email
    },
    updateItem: (state, item) => state.items.child(item.sn).set(item)
  },

  actions: {
    login: (context, user) => {
      return Firebase.auth()
        .signInWithEmailAndPassword(user.email, user.password)
        .then( res => {
          console.log('logged as', res.user.email)
          context.commit('setUser')
        })
    },
    logout: context => {
      return Firebase.auth().signOut()
      .catch( err => console.error('logout failed', err.message))
      .then( () => {
        console.log('signed out')
        context.commit('setUser')
      })
    },
    addItem: (context, item) => context.commit('updateItem', item),
    editItem: (context, item) => context.commit('updateItem', item)
  }
})

export default store