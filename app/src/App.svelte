<script lang="ts">
let n = 10000;
let pi: number | null = null;
let loading = false;
let error = "";

async function estimatePi() {
	loading = true;
	error = "";
	pi = null;

	try {
		const response = await fetch("http://localhost:8000/generate-points", {
			method: "POST",
			headers: { "Content-Type": "application/json" },
			body: JSON.stringify({ n }),
		});

		if (!response.ok) throw new Error("Failed to fetch points");

		const { points } = await response.json();
		const inside = points.filter(
			([x, y]: number[]) => x * x + y * y <= 1,
		).length;
		pi = 4 * (inside / n);
	} catch (e) {
		error = (e as Error).message;
	} finally {
		loading = false;
	}
}
</script>

<main>
  <h1>Monte Carlo Pi Estimation</h1>

  <label>
    Number of random points:
    <input type="number" bind:value={n} min="10" />
  </label>

  <button on:click={estimatePi} disabled={loading}>
    {loading ? 'Estimating...' : 'Estimate Pi'}
  </button>

  {#if pi !== null}
    <p>Estimated Pi: <strong>{pi}</strong></p>
  {/if}

  {#if error}
    <p style="color: red;">Error: {error}</p>
  {/if}
</main>

<style>
  main {
    padding: 2rem;
    font-family: sans-serif;
    max-width: 400px;
    margin: auto;
    text-align: center;
  }

  input {
    margin-top: 0.5rem;
    padding: 0.4rem;
    width: 100%;
  }

  button {
    margin-top: 1rem;
    padding: 0.5rem 1rem;
    font-size: 1rem;
  }

  p {
    margin-top: 1rem;
  }
</style>
