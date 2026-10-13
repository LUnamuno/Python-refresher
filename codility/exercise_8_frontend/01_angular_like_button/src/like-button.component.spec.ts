import { ComponentFixture, TestBed } from '@angular/core/testing';
import { LikeButtonComponent } from './like-button.component';

describe('LikeButtonComponent', () => {
  let fixture: ComponentFixture<LikeButtonComponent>;

  const button = (): HTMLButtonElement =>
    fixture.nativeElement.querySelector('button.like-button');
  const counter = (): HTMLSpanElement =>
    fixture.nativeElement.querySelector('.likes-counter');
  const click = (): void => {
    button().click();
    fixture.detectChanges();
  };

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [LikeButtonComponent],
    }).compileComponents();
    fixture = TestBed.createComponent(LikeButtonComponent);
    fixture.detectChanges();
  });

  describe('1. There should be a like button', () => {
    it('renders a button with the like-button class', () => {
      expect(button()).not.toBeNull();
      expect(button().classList.contains('like-button')).toBe(true);
    });

    it('content has the format "Like | 100"', () => {
      expect(button().textContent).toBe('Like | 100');
    });

    it('wraps the number of likes in span.likes-counter inside the button', () => {
      expect(counter().tagName).toBe('SPAN');
      expect(button().contains(counter())).toBe(true);
      expect(counter().textContent).toBe('100');
    });

    it('is not liked at the start', () => {
      expect(button().classList.contains('liked')).toBe(false);
    });
  });

  describe('2. Users can add a like', () => {
    it('increases the counter by one', () => {
      click();
      expect(counter().textContent).toBe('101');
      expect(button().textContent).toBe('Like | 101');
    });

    it('adds the liked class and keeps like-button', () => {
      click();
      expect(button().classList.contains('like-button')).toBe(true);
      expect(button().classList.contains('liked')).toBe(true);
    });
  });

  describe('3. Users can undo their like', () => {
    it('decreases the counter by one', () => {
      click();
      click();
      expect(counter().textContent).toBe('100');
    });

    it('removes the liked class', () => {
      click();
      click();
      expect(button().classList.contains('liked')).toBe(false);
      expect(button().classList.contains('like-button')).toBe(true);
    });

    it('keeps toggling correctly over several clicks', () => {
      [101, 100, 101, 100, 101].forEach((value) => {
        click();
        expect(counter().textContent).toBe(String(value));
        expect(button().classList.contains('liked')).toBe(value === 101);
      });
    });
  });
});
