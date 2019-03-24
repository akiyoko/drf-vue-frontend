<template>
  <!-- ヘッダナビゲーション -->
  <div id="header">
    <b-navbar type="dark" variant="dark">
      <a class="navbar-brand" href="/">
        <img src="@/assets/images/logo.png" width="120">
      </a>
      <b-navbar-nav class="ml-auto" v-if="$route.meta.requiresAuth">
        <b-nav-item-dropdown right v-if="$store.state.user.loggedIn">
          <template slot="button-content">{{ $store.state.user.username }}</template>
          <b-dropdown-item href="#" @click="linkLogout">ログアウト</b-dropdown-item>
        </b-nav-item-dropdown>
        <b-nav-item href="#" @click="linkLogin" v-else>ログイン</b-nav-item>
      </b-navbar-nav>
    </b-navbar>
  </div>
</template>

<script>
  import userService from '@/services/userService'

  export default {
    methods: {
      // ログアウトリンク押下時に呼び出されるメソッド
      linkLogout: function () {
        userService.logout()
        this.$store.commit('message/set', { info: 'ログアウトしました。' })
        this.$router.replace('/login')
      },
      // ログインリンク押下時に呼び出されるメソッド
      linkLogin: function () {
        this.$store.commit('message/clear')
        this.$router.replace('/login')
      }
    }
  }
</script>

<style scoped>
</style>
