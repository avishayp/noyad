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

function getFirebaseAuthUser() {
  let user = Firebase.auth().currentUser
  return user && user.email
}

function updateStateItems(stat) {
  Firebase.database().ref('items')
  .once('value')
  .then( snap => {
    stat.items = snap.val()
  })
  .catch( err => { console.error(err)})
}

const store = new Vuex.Store({

  state: {
    user: null,
    items: {}
  },

  getters: {
    userName: state => {
      return state.user && state.user.split('@')[0]
    },
    items: state => {
      updateStateItems(state)
      return state.items 
    }
  },

  mutations: {
    waitUser: (state, callback) => {
      Firebase.auth().onAuthStateChanged( user => {
        state.user = user && user.email
        callback()
      })
    },
    setUser: state => {
      state.user = getFirebaseAuthUser()
    },
    update: (state, item) => {
      var itemId = item.sn
      Firebase.database().ref('items/' + itemId)
      .set(item)
    }
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
    addItem: (context, item) => {
      context.commit('update', item)
    },
    editItem: (context, item) => {
      context.commit('update', item)
    }
  }
})

export default store