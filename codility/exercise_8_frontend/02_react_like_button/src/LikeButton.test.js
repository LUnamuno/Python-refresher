import React from 'react';
import { render, fireEvent } from '@testing-library/react';
import LikeButton from './LikeButton';

function setup() {
  const { container } = render(<LikeButton />);
  const button = container.querySelector('button.like-button');
  const counter = () => container.querySelector('.likes-counter');
  return { container, button, counter };
}

describe('1. There should be a like button', () => {
  test('renders a button with the like-button class', () => {
    const { button } = setup();
    expect(button).not.toBeNull();
    expect(button.classList.contains('like-button')).toBe(true);
  });

  test('content has the format "Like | 100"', () => {
    const { button } = setup();
    expect(button.textContent).toBe('Like | 100');
  });

  test('the number of likes is wrapped in a span.likes-counter inside the button', () => {
    const { button, counter } = setup();
    expect(counter().tagName).toBe('SPAN');
    expect(button.contains(counter())).toBe(true);
    expect(counter().textContent).toBe('100');
  });

  test('is not liked at the start', () => {
    const { button } = setup();
    expect(button.classList.contains('liked')).toBe(false);
  });
});

describe('2. Users can add a like', () => {
  test('clicking increases the counter by one', () => {
    const { button, counter } = setup();
    fireEvent.click(button);
    expect(counter().textContent).toBe('101');
    expect(button.textContent).toBe('Like | 101');
  });

  test('clicking adds the liked class and keeps like-button', () => {
    const { button } = setup();
    fireEvent.click(button);
    expect(button.classList.contains('like-button')).toBe(true);
    expect(button.classList.contains('liked')).toBe(true);
  });
});

describe('3. Users can undo their like', () => {
  test('clicking again decreases the counter by one', () => {
    const { button, counter } = setup();
    fireEvent.click(button);
    fireEvent.click(button);
    expect(counter().textContent).toBe('100');
  });

  test('clicking again removes the liked class', () => {
    const { button } = setup();
    fireEvent.click(button);
    fireEvent.click(button);
    expect(button.classList.contains('liked')).toBe(false);
    expect(button.classList.contains('like-button')).toBe(true);
  });

  test('keeps toggling correctly over several clicks', () => {
    const { button, counter } = setup();
    const expected = [101, 100, 101, 100, 101];
    expected.forEach((value) => {
      fireEvent.click(button);
      expect(counter().textContent).toBe(String(value));
      expect(button.classList.contains('liked')).toBe(value === 101);
    });
  });
});
