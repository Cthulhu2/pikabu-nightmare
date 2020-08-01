import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

import {setDomain} from './gen/userApi.js'

const getUrl = window.location;
setDomain(getUrl.protocol + "//" + getUrl.host + "/back")

// To local development, beware:
// Cross-Origin Request Blocked: The Same Origin Policy disallows reading
// the remote resource at http://127.0.0.1:5000/back/u/test.
// (Reason: CORS request did not succeed)
//setDomain("http://127.0.0.1:5000/back")

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
