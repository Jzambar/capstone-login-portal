<script setup>
// Root layout component
</script>

<template>
  <!-- This displays whatever page matches your current URL route (like LoginView) -->
  <router-view />
</template>

<style>
/* Basic global resets */
body {
  margin: 0;
  padding: 0;
  font-family: system-ui, -apple-system, sans-serif;
  background-color: #0f172a;
}
</style>