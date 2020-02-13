import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { EssaySignupComponent } from './essay-signup.component';

describe('EssaySignupComponent', () => {
  let component: EssaySignupComponent;
  let fixture: ComponentFixture<EssaySignupComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ EssaySignupComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(EssaySignupComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
