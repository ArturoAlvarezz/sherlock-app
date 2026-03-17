<script setup>
import { ref, onMounted } from 'vue'
import { Search, History, Terminal, ExternalLink, ShieldAlert, Cpu } from 'lucide-vue-next'

const username = ref('')
const results = ref([])
const isSearching = ref(false)
const statusMessage = ref('READY_FOR_SCAN')
const apiUrl = import.meta.env.VITE_API_URL || 'http://localhost:8000'

const startSearch = () => {
  if (!username.value || isSearching.value) return

  results.value = []
  isSearching.value = true
  statusMessage.value = 'INITIALIZING_PROBE...'

  const eventSource = new EventSource(`${apiUrl}/search/${username.value}`)

  eventSource.addEventListener('status', (e) => {
    statusMessage.value = e.data.toUpperCase().replace(/\s+/g, '_')
  })

  eventSource.addEventListener('match', (e) => {
    const match = JSON.parse(e.data)
    results.value.unshift(match)
  })

  eventSource.addEventListener('done', (e) => {
    isSearching.value = false
    statusMessage.value = 'SCAN_COMPLETE'
    eventSource.close()
  })

  eventSource.addEventListener('error', (e) => {
    console.error("SSE Error:", e)
    isSearching.value = false
    statusMessage.value = 'CONNECTION_LOST'
    eventSource.close()
  })
}
</script>

<template>
  <div class="min-h-screen p-4 md:p-8 flex flex-col items-center">
    <!-- Header -->
    <header class="w-full max-w-5xl flex flex-col md:flex-row justify-between items-center mb-12 gap-6">
      <div class="flex items-center gap-4">
        <Cpu class="text-cyber-purple w-12 h-12 drop-shadow-neon" />
        <div>
          <h1 class="text-4xl font-bold tracking-tighter glitch-text">SHERLOCK_WEB</h1>
          <p class="text-cyber-purple text-xs tracking-[0.3em]">CYBER_INTEL_SYSTEM_v1.0</p>
        </div>
      </div>
      
      <div class="flex flex-col items-end">
        <div class="flex items-center gap-2 text-cyber-neon mb-1">
          <div class="w-2 h-2 rounded-full bg-cyber-neon animate-pulse"></div>
          <span class="text-sm font-bold">{{ statusMessage }}</span>
        </div>
        <div class="text-[10px] text-cyber-purple opacity-70">
          UPLINK: {{ apiUrl }}
        </div>
      </div>
    </header>

    <main class="w-full max-w-6xl grid grid-cols-1 lg:grid-cols-12 gap-8">
      <div class="lg:col-span-12 space-y-8 max-w-2xl mx-auto w-full">
        <!-- Search Input -->
        <section class="cyber-card">
          <h2 class="text-lg font-bold mb-4 flex items-center gap-2">
            <Search class="w-5 h-5" /> INPUT_TARGET
          </h2>
          <div class="relative">
            <input 
              v-model="username" 
              @keyup.enter="startSearch"
              placeholder="ENTER_USERNAME..." 
              class="cyber-input mb-6"
              :disabled="isSearching"
            />
            <button 
              @click="startSearch" 
              class="cyber-button w-full"
              :disabled="isSearching || !username"
            >
              <span v-if="!isSearching">INITIALIZE_SCAN</span>
              <span v-else class="flex items-center justify-center gap-2">
                <span class="animate-spin text-xl">/</span> SCANNING...
              </span>
            </button>
          </div>
        </section>
      </div>

      <!-- Terminal Column (Now Full Width) -->
      <div class="lg:col-span-12">
        <section class="cyber-card h-[600px] flex flex-col relative">
          <!-- Terminal Header -->
          <div class="flex items-center justify-between border-b border-cyber-purple pb-2 mb-4">
            <div class="flex items-center gap-2 text-cyber-purple">
              <Terminal class="w-5 h-5" />
              <span class="text-sm font-bold">TERMINAL_OUTPUT</span>
            </div>
            <div class="flex gap-2">
              <div class="w-3 h-3 border border-cyber-purple"></div>
              <div class="w-3 h-3 border border-cyber-purple"></div>
              <div class="w-3 h-3 border border-cyber-purple bg-cyber-purple"></div>
            </div>
          </div>

          <!-- Results List -->
          <div class="overflow-y-auto flex-grow space-y-2 font-mono text-sm">
            <div v-if="results.length === 0 && !isSearching" class="h-full flex flex-col items-center justify-center opacity-30">
              <ShieldAlert class="w-16 h-16 mb-4" />
              <p>AWAITING_UPLINK_COMMAND</p>
            </div>

            <div v-for="(res, idx) in results" :key="idx" 
                 class="flex items-center gap-4 py-2 border-b border-cyber-purple/10 hover:bg-cyber-purple/5 group px-2 animate-in fade-in slide-in-from-left duration-300">
              <span class="text-cyber-neon font-bold min-w-[120px]">{{ res.site }}:</span>
              <a :href="res.url" target="_blank" class="text-cyber-purple truncate hover:text-white transition-colors flex-grow flex items-center gap-2">
                {{ res.url }}
                <ExternalLink class="w-3 h-3 opacity-0 group-hover:opacity-100 transition-opacity" />
              </a>
              <span class="text-[10px] text-green-500 font-bold bg-green-500/10 px-1">FOUND</span>
            </div>
            
            <!-- Scanning Animation -->
            <div v-if="isSearching" class="py-4 text-cyber-purple animate-pulse flex items-center gap-2">
              <span class="inline-block w-2 h-4 bg-cyber-purple animate-ping"></span>
              SCANNING_VIRTUAL_SPACE...
            </div>
          </div>

          <!-- Grid Background Effect -->
          <div class="absolute inset-0 pointer-events-none opacity-[0.03]" 
               style="background-size: 20px 20px; background-image: linear-gradient(to right, #bc13fe 1px, transparent 1px), linear-gradient(to bottom, #bc13fe 1px, transparent 1px);">
          </div>
        </section>
      </div>
    </main>

    <!-- Footer Decoration -->
    <footer class="mt-12 w-full max-w-6xl flex justify-between items-center text-[10px] text-cyber-purple/50 border-t border-cyber-purple/20 pt-4">
      <div>SEC_LEVEL: ALPHA_7</div>
      <div>ENCRYPTION: AES_256_GCM</div>
      <div>CORE_TEMP: 32°C</div>
    </footer>
  </div>
</template>

<style>
.animate-in {
  animation-duration: 0.3s;
  animation-fill-mode: both;
}

@keyframes fade-in {
  from { opacity: 0; }
  to { opacity: 1; }
}

@keyframes slide-in-from-left {
  from { transform: translateX(-10px); }
  to { transform: translateX(0); }
}

.fade-in { animation-name: fade-in; }
.slide-in-from-left { animation-name: slide-in-from-left; }
</style>
