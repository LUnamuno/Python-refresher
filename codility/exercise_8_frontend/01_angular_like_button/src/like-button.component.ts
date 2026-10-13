import { Component } from '@angular/core';

@Component({
  selector: 'app-like-button',
  template: `<button class="like-button" [class.liked]="liked" (click)="toggleLike()">Like | <span class="likes-counter">{{ likes }}</span></button>`,
})
export class LikeButtonComponent {
  likes = 100;
  liked = false;

  toggleLike(): void {
    // A click toggles the like: +1 when adding it, -1 when undoing it.
    this.likes += this.liked ? -1 : 1;
    this.liked = !this.liked;
  }
}
