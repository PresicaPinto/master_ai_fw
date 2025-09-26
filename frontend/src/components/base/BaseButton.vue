<template>
  <button class="base-button">
    <slot></slot>
  </button>
</template>

<script>
export default {
  name: 'BaseButton',
};
</script>

<style scoped>
.base-button {
  padding: 8px 16px;
  border: 1px solid #ccc;
  border-radius: 4px;
  cursor: pointer;
}
</style>
