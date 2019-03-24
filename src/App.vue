<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<script>
  import userService from '@/services/userService'

  export default {
    mounted: function () {
      const token = localStorage.getItem('access')
      if (token != null) {
        console.log('mounted ... JWT is found. So, try to get user info.')
        userService.getUser()
          .then(() => {
            next()
          })
      }
    }
  }
</script>

<style>
  #app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    color: #2c3e50;
  }

  main.container {
    border: 1px solid #cccccc;
    margin-top: 4em;
    padding: 2em;
    width: 600px;
  }
</style>
