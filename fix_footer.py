import sys

with open("src/pages/index.astro", "r") as f:
    text = f.read()

old_footer = """<footer class="py-10 px-4 bg-foreground text-background/80"><div class="max-w-6xl mx-auto text-center space-y-6"><p class="text-sm">© 2025-2026 IKASI Bodywork™ - Alle Rechte vorbehalten</p><nav class="flex flex-wrap justify-center gap-x-4 gap-y-2 text-sm"><span class="flex items-center gap-4"><a href="https://www.ikasi-bodywork.com/" class="hover:text-background transition-colors">Startseite</a><span class="text-background/30">|</span></span><span class="flex items-center gap-4"><a href="https://www.ikasi-bodywork.com/kontakt" class="hover:text-background transition-colors">Kontakt</a><span class="text-background/30">|</span></span><span class="flex items-center gap-4"><a href="https://www.ikasi-bodywork.com/datenschutz" class="hover:text-background transition-colors">Datenschutz</a><span class="text-background/30">|</span></span><span class="flex items-center gap-4"><a href="https://www.ikasi-bodywork.com/rechtliches" class="hover:text-background transition-colors">Rechtliches</a><span class="text-background/30">|</span></span><span class="flex items-center gap-4"><a href="https://www.ikasi-bodywork.com/agbs" class="hover:text-background transition-colors">Allgemeine Geschäftsbedingungen</a><span class="text-background/30">|</span></span><span class="flex items-center gap-4"><a href="https://www.ikasi-bodywork.com/widerruf" class="hover:text-background transition-colors">Widerruf</a><span class="text-background/30">|</span></span><span class="flex items-center gap-4"><a href="https://www.ikasi-bodywork.com/impressum" class="hover:text-background transition-colors">Impressum</a></span></nav></div></footer>"""

new_footer = """<footer class="py-12 px-6 bg-card border-t border-border mt-10">
  <div class="max-w-6xl mx-auto">
    <div class="grid grid-cols-1 md:grid-cols-3 gap-10 lg:gap-16 mb-12">
      <!-- Left Column -->
      <div class="space-y-6">
        <div>
          <h3 class="font-serif text-xl font-medium text-primary mb-2">IKASI Bodywork™</h3>
          <p class="text-foreground/70 text-sm leading-relaxed">Entgiftung und Aufbau – 60 Tage, die dein komplettes System verändern.</p>
        </div>
        <div>
          <a href="https://www.checkout-ds24.com/product/632732/checkout" target="_blank" rel="noopener noreferrer" class="inline-flex items-center justify-center gap-2 h-10 bg-primary hover:bg-gold-dark text-primary-foreground font-semibold px-6 py-2 text-sm rounded-lg shadow-soft transition-all btn-shine">KURS STARTEN <span class="ml-1">→</span></a>
        </div>
        <div class="pt-2">
          <a href="https://www.instagram.com/ikasi.bodywork/" target="_blank" rel="noopener noreferrer" class="inline-flex items-center justify-center w-10 h-10 rounded-full bg-foreground/5 hover:bg-primary/10 text-foreground/70 hover:text-primary transition-colors">
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-instagram"><rect width="20" height="20" x="2" y="2" rx="5" ry="5"></rect><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path><line x1="17.5" x2="17.51" y1="6.5" y2="6.5"></line></svg>
          </a>
        </div>
      </div>

      <!-- Middle Column -->
      <div>
        <h4 class="font-semibold text-xs tracking-wider uppercase text-foreground mb-4">Navigation</h4>
        <ul class="space-y-3 text-sm text-foreground/70">
          <li><a href="https://www.ikasi-bodywork.com/" class="hover:text-primary transition-colors">Startseite</a></li>
          <li><a href="https://www.ikasi-bodywork.com/#prozess" class="hover:text-primary transition-colors">Der Prozess</a></li>
          <li><a href="https://www.ikasi-bodywork.com/#fuer-wen" class="hover:text-primary transition-colors">Für wen</a></li>
          <li><a href="https://www.checkout-ds24.com/product/632732/checkout" target="_blank" rel="noopener noreferrer" class="hover:text-primary transition-colors">Entgiftung starten</a></li>
          <li><a href="https://www.ikasi-bodywork.com/kontakt" class="hover:text-primary transition-colors">Kontakt</a></li>
        </ul>
      </div>

      <!-- Right Column -->
      <div>
        <h4 class="font-semibold text-xs tracking-wider uppercase text-foreground mb-4">Rechtliches</h4>
        <ul class="space-y-3 text-sm text-foreground/70">
          <li><a href="https://www.ikasi-bodywork.com/impressum" class="hover:text-primary transition-colors">Impressum</a></li>
          <li><a href="https://www.ikasi-bodywork.com/datenschutz" class="hover:text-primary transition-colors">Datenschutz</a></li>
          <li><a href="https://www.ikasi-bodywork.com/rechtliches" class="hover:text-primary transition-colors">Rechtliches</a></li>
          <li><a href="https://www.ikasi-bodywork.com/agbs" class="hover:text-primary transition-colors">Allgemeine Geschäftsbedingungen</a></li>
          <li><a href="https://www.ikasi-bodywork.com/widerruf" class="hover:text-primary transition-colors">Widerruf</a></li>
        </ul>
      </div>
    </div>

    <!-- Bottom Bar -->
    <div class="pt-8 border-t border-border/60 flex flex-col md:flex-row items-center justify-between gap-4 text-xs text-foreground/60">
      <p>© 2025 IKASI Bodywork™ — Alle Rechte vorbehalten</p>
      <p>Made with <span class="text-primary mx-0.5">❤</span> in Deutschland von <a href="https://web-eleganz.de" target="_blank" rel="noopener noreferrer" class="font-medium text-foreground/80 hover:text-primary transition-colors link-underline">Web-Eleganz</a></p>
    </div>
  </div>
</footer>"""

if old_footer in text:
    text = text.replace(old_footer, new_footer)
    print("Replaced footer successfully.")
else:
    print("Could not find old footer HTML!")

with open("src/pages/index.astro", "w") as f:
    f.write(text)

