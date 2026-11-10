<script setup>
import { ref } from 'vue'

// Local state for UI feedback only
const email = ref('')
const password = ref('')
const isSubmitted = ref(false)

const handleLoginClick = () => {
  if (email.value) {
    isSubmitted.value = true
  }
}
</script>

<template>
  <div class="login-container">
    <div class="login-card">
      <div class="header-badge">Russellville Department of Sustainability</div>
      <h2>City Portal</h2>
      <p class="subtitle">Sign in to access municipal tracking tools</p>

      <!-- Success message banner -->
      <div v-if="isSubmitted" class="success-banner">
        Login screen submitted!
      </div>

      <form @submit.prevent="handleLoginClick">
        <div class="form-group">
          <label for="email">City Email</label>
          <input 
            id="email" 
            type="email" 
            v-model="email" 
            placeholder="official@russellville.gov" 
            required 
          />
        </div>

        <div class="form-group">
          <label for="password">Password</label>
          <input 
            id="password" 
            type="password" 
            v-model="password" 
            placeholder="--------" 
            required 
          />
        </div>

        <button type="submit" class="login-btn">
          Sign In
        </button>
      </form>

      <div class="footer-links">
        <a href="#" @click.prevent>Forgot password?</a>
        <a href="#" @click.prevent>Request department access</a>
      </div>
    </div>
  </div>
</template>

<style scoped>
.login-container {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background-color: #0f172a;
  font-family: system-ui, -apple-system, sans-serif;
  padding: 1rem;
}
.login-card {
  background: #ffffff;
  padding: 2.5rem;
  border-radius: 12px;
  box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.3);
  width: 100%;
  max-width: 420px;
  box-sizing: border-box;
}
.header-badge {
  display: inline-block;
  background-color: #e0f2fe;
  color: #0369a1;
  font-size: 0.75rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  padding: 0.25rem 0.6rem;
  border-radius: 9999px;
  margin-bottom: 1rem;
}
h2 {
  margin: 0 0 0.25rem 0;
  color: #0f172a;
  font-size: 1.75rem;
}
.subtitle {
  color: #64748b;
  font-size: 0.9rem;
  margin-bottom: 1.5rem;
}
.form-group {
  margin-bottom: 1.2rem;
  text-align: left;
}
label {
  display: block;
  font-size: 0.85rem;
  font-weight: 600;
  color: #334155;
  margin-bottom: 0.4rem;
}
input {
  width: 100%;
  padding: 0.75rem;
  border: 1px solid #cbd5e1;
  border-radius: 6px;
  font-size: 1rem;
  box-sizing: border-box;
  transition: border-color 0.2s;
}
input:focus {
  outline: none;
  border-color: #2563eb;
  box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.15);
}
.login-btn {
  width: 100%;
  padding: 0.75rem;
  background-color: #2563eb;
  color: white;
  border: none;
  border-radius: 6px;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: background-color 0.2s;
  margin-top: 0.5rem;
}
.login-btn:hover {
  background-color: #1d4ed8;
}
.success-banner {
  background-color: #d1fae5;
  color: #065f46;
  padding: 0.75rem;
  border-radius: 6px;
  font-size: 0.9rem;
  margin-bottom: 1.2rem;
  font-weight: 500;
}
.footer-links {
  display: flex;
  justify-content: space-between;
  margin-top: 1.5rem;
  font-size: 0.85rem;
}
.footer-links a {
  color: #2563eb;
  text-decoration: none;
}
.footer-links a:hover {
  text-decoration: underline;
}
</style>