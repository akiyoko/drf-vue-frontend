<template>
  <!-- メッセージエリア -->
  <div id="messages">
    <b-alert
      variant="danger" show
      v-show="$store.state.message.error" class="mb-0">
      {{ $store.state.message.error }}
    </b-alert>
    <b-alert
      variant="warning" show
      v-show="$store.state.message.warnings.length > 0" class="mb-0">
      <p v-for="v in $store.state.message.warnings" class="mb-0">{{ v[1][0] }}</p>
    </b-alert>
    <b-alert
      variant="info" show
      v-show="$store.state.message.info" class="mb-0">
      {{ $store.state.message.info }}
    </b-alert>
  </div>
</template>

<script>
</script>

<style scoped>
</style>
