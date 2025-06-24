<script lang="ts">
  let count = 0;
</script>

<main>
  <h1>Hello from App.svelte 👋</h1>
  <button on:click={() => count++}>
    Count: {count}
  </button>
</main>

<style>
  main {
    padding: 2rem;
    font-family: sans-serif;
    text-align: center;
  }
</style>
