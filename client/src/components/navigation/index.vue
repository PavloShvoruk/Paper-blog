<template>
  <nav class="border fixed split-nav">
    <div class="nav-brand">
      <h3>
        <a href="#">Paper Blog</a>
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
          <li>
            <a href="#">My Articles</a>
          </li>
          <li>
            <a href="#">Register</a>
          </li>
          <li>
            <a href="#">Login</a>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<style scoped>
</style>


<script>
export default {
  name: "navigation"
};
</script>