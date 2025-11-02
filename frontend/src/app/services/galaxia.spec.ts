import { TestBed } from '@angular/core/testing';

import { Galaxia } from './galaxia';

describe('Galaxia', () => {
  let service: Galaxia;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(Galaxia);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
