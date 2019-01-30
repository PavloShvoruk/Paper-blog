<template>
  <nav class="border fixed split-nav">
    <div class="nav-brand">
      <h3>
        <router-link to="/">Paper Blog</router-link>
      </h3>
    </div>
    <div class="collapsible">
      <input id="collapsible1" type="checkbox" name="collapsible1">
      <button>
        <label for="collapsible1">
          <div class="bar1"></div>
          <div class="bar2"></div>
          <div class="bar3"></div>
        </label>
      </button>
      <div class="collapsible-body">
        <ul class="inline">
          <li v-if="isAuthenticated">
            <router-link to>{{ name }}</router-link>
          </li>
          <li v-if="!isAuthenticated && !authLoading">
            <router-link to="/login">Login</router-link>
          </li>
          <li v-if="isAuthenticated" @click="logout">
            <a href>Logout</a>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script>
import { mapGetters, mapState } from "vuex";
import { AUTH_LOGOUT } from "../../store/actions/auth.js";

export default {
  name: "navigation",
  methods: {
    logout() {
      this.$store.dispatch(AUTH_LOGOUT).then(() => this.$router.push("/"));
    }
  },
  computed: {
    ...mapGetters(["getProfile", "isAuthenticated", "isProfileLoaded"]),
    ...mapState({
      authLoading: state => state.auth.status === "loading",
      name: state => `${state.user.profile}`
    })
  }
};
</script>