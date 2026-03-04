import sys
import re

with open("src/pages/index.astro", "r") as f:
    text = f.read()

text = text.replace(
    'px-10 py-6 text-lg',
    'px-6 py-4 md:px-10 md:py-6 text-base md:text-lg'
)

text = text.replace(' h-10 bg-primary', ' bg-primary')
text = text.replace('h-10 bg-primary', 'bg-primary')

text = text.replace(
    '60 Tage Anleitung, Begleitung und Transformation – für nur 99 €.',
    '60 Tage Anleitung, Begleitung und Transformation – regulär <span class="line-through text-muted-foreground mr-1">111 €</span>, jetzt kurzfristig für 99 €.'
)

old_slider = """<div class="sm:hidden"><div class="relative"><button class="absolute left-0 top-1/2 -translate-y-1/2 -translate-x-2 z-10 w-10 h-10 rounded-full bg-card border border-border shadow-soft flex items-center justify-center text-foreground/70 hover:text-primary hover:border-primary transition-all" aria-label="Vorheriges Testimonial"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-chevron-left w-5 h-5"><path d="m15 18-6-6 6-6"></path></svg></button><button class="absolute right-0 top-1/2 -translate-y-1/2 translate-x-2 z-10 w-10 h-10 rounded-full bg-card border border-border shadow-soft flex items-center justify-center text-foreground/70 hover:text-primary hover:border-primary transition-all" aria-label="Nächstes Testimonial"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-chevron-right w-5 h-5"><path d="m9 18 6-6-6-6"></path></svg></button><div class="px-6"><div class="ikasi-card p-5 transition-all duration-300 hover:shadow-elevated hover:-translate-y-2 hover:scale-[1.02] cursor-default h-full"><blockquote class="text-foreground/80 italic text-sm leading-relaxed mb-4">"Mein Gesicht, mein Bauch, mein ganzer Körper - plötzlich wirkt alles lebendiger."</blockquote><cite class="text-primary font-medium text-sm not-italic">H. L., 32</cite></div></div></div><div class="flex justify-center gap-2 mt-4"><button class="w-2 h-2 rounded-full transition-all duration-300 bg-primary w-4" aria-label="Testimonial 1"></button><button class="w-2 h-2 rounded-full transition-all duration-300 bg-border hover:bg-primary/50" aria-label="Testimonial 2"></button><button class="w-2 h-2 rounded-full transition-all duration-300 bg-border hover:bg-primary/50" aria-label="Testimonial 3"></button><button class="w-2 h-2 rounded-full transition-all duration-300 bg-border hover:bg-primary/50" aria-label="Testimonial 4"></button><button class="w-2 h-2 rounded-full transition-all duration-300 bg-border hover:bg-primary/50" aria-label="Testimonial 5"></button><button class="w-2 h-2 rounded-full transition-all duration-300 bg-border hover:bg-primary/50" aria-label="Testimonial 6"></button><button class="w-2 h-2 rounded-full transition-all duration-300 bg-border hover:bg-primary/50" aria-label="Testimonial 7"></button><button class="w-2 h-2 rounded-full transition-all duration-300 bg-border hover:bg-primary/50" aria-label="Testimonial 8"></button></div></div>"""

new_slider = """<div class="sm:hidden relative testimonial-slider-container">
  <button class="testi-prev absolute left-0 top-1/2 -translate-y-1/2 -translate-x-2 z-10 w-10 h-10 rounded-full bg-card border border-border shadow-soft flex items-center justify-center text-foreground/70 hover:text-primary hover:border-primary transition-all" aria-label="Vorheriges Testimonial"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-chevron-left w-5 h-5"><path d="m15 18-6-6 6-6"></path></svg></button>
  <button class="testi-next absolute right-0 top-1/2 -translate-y-1/2 translate-x-2 z-10 w-10 h-10 rounded-full bg-card border border-border shadow-soft flex items-center justify-center text-foreground/70 hover:text-primary hover:border-primary transition-all" aria-label="Nächstes Testimonial"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-chevron-right w-5 h-5"><path d="m9 18 6-6-6-6"></path></svg></button>
  
  <div class="overflow-hidden px-5">
    <div class="flex transition-transform duration-300 testi-track">
      {testimonials.map(t => (
        <div class="w-full shrink-0 px-2 box-border">
          <div class="ikasi-card p-5 h-full transition-all duration-300">
            <blockquote class="text-foreground/80 italic text-sm leading-relaxed mb-4">"{t.quote}"</blockquote>
            <cite class="text-primary font-medium text-sm not-italic">{t.name}</cite>
          </div>
        </div>
      ))}
    </div>
  </div>
  
  <div class="flex justify-center gap-2 mt-4 testi-dots">
    {testimonials.map((_, i) => (
      <button class={`w-2 h-2 rounded-full transition-all duration-300 ${i === 0 ? 'bg-primary w-4' : 'bg-border hover:bg-primary/50'}`} aria-label={`Testimonial ${i + 1}`} data-index={i}></button>
    ))}
  </div>
</div>""".replace("\n", "")

if old_slider in text:
    text = text.replace(old_slider, new_slider)
else:
    print("Could not find old slider HTML!")

js_script = """
  // Testimonial Slider JS
  document.addEventListener('DOMContentLoaded', () => {
    const track = document.querySelector('.testi-track');
    const dots = document.querySelectorAll('.testi-dots button');
    let curSlide = 0;
    
    if (!track || !dots.length) return;

    function updateSlider() {
      track.style.transform = `translateX(-${curSlide * 100}%)`;
      dots.forEach((d, i) => {
        if (i === curSlide) {
          d.className = 'w-2 h-2 rounded-full transition-all duration-300 bg-primary w-4';
        } else {
          d.className = 'w-2 h-2 rounded-full transition-all duration-300 bg-border hover:bg-primary/50';
        }
      });
    }

    const prevBtn = document.querySelector('.testi-prev');
    const nextBtn = document.querySelector('.testi-next');

    if(prevBtn) {
      prevBtn.addEventListener('click', () => {
        curSlide = (curSlide - 1 + dots.length) % dots.length;
        updateSlider();
      });
    }

    if(nextBtn) {
      nextBtn.addEventListener('click', () => {
        curSlide = (curSlide + 1) % dots.length;
        updateSlider();
      });
    }

    dots.forEach((dot) => {
      dot.addEventListener('click', (e) => {
        curSlide = parseInt(e.target.getAttribute('data-index'));
        updateSlider();
      });
    });
    
    let touchStartX = 0;
    let touchEndX = 0;

    track.addEventListener('touchstart', e => {
      touchStartX = e.changedTouches[0].screenX;
    }, {passive: true});

    track.addEventListener('touchend', e => {
      touchEndX = e.changedTouches[0].screenX;
      handleSwipe();
    }, {passive: true});

    function handleSwipe() {
      if (touchEndX < touchStartX - 40) {
        curSlide = (curSlide + 1) % dots.length;
        updateSlider();
      }
      if (touchEndX > touchStartX + 40) {
        curSlide = (curSlide - 1 + dots.length) % dots.length;
        updateSlider();
      }
    }
  });
"""

insert_point = '</script>\n\n<script src="https://unpkg.com/@studio-freight/lenis@1.0.42/dist/lenis.min.js">'
if insert_point in text:
    text = text.replace(insert_point, js_script + insert_point)
else:
    print("Could not find insertion point for JS!")

desktop_pattern = re.compile(r'<div class="hidden sm:grid sm:grid-cols-2 lg:grid-cols-4 gap-4">.*?</div><div class="sm:hidden', re.DOTALL)
new_desktop = '<div class="hidden sm:grid sm:grid-cols-2 lg:grid-cols-4 gap-4">{testimonials.map(t => (<div class="ikasi-card p-5 transition-all duration-300 hover:shadow-elevated hover:-translate-y-2 hover:scale-[1.02] cursor-default h-full"><blockquote class="text-foreground/80 italic text-sm leading-relaxed mb-4">"{t.quote}"</blockquote><cite class="text-primary font-medium text-sm not-italic">{t.name}</cite></div>))}</div><div class="sm:hidden'.replace('\n', '')

if desktop_pattern.search(text):
    text = desktop_pattern.sub(new_desktop, text)
else:
    print("Could not find desktop grid HTML!")

with open("src/pages/index.astro", "w") as f:
    f.write(text)

