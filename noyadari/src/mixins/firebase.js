
import Firebase from "firebase";
var config = {
    apiKey: "AIzaSyA2-829SxwBT5bab5zy4HaWapjLFWZ_WMo",
    authDomain: "vue-project-9e30c.firebaseapp.com",
    databaseURL: "https://vue-project-9e30c.firebaseio.com",
    projectId: "vue-project-9e30c",
    storageBucket: "vue-project-9e30c.appspot.com",
    messagingSenderId: "855934020751"
  };
  
  let app = Firebase.initializeApp(config);
  export const db = app.database();