import { describe, it } from 'mocha';
import Test from 'chai';
import { vm } from './versions_manager.js';

describe('VersionManager tests', () => {
    it('Initialization tests', () => {
        Test.assert.equal(vm().release(), '0.0.1', 'Default initial version');
        Test.assert.equal(vm('').release(), '0.0.1', 'Default initial version');
        Test.assert.equal(vm('1.2.3').release(), '1.2.3', 'No version changes');
        Test.assert.equal(
            vm('1.2.3.4').release(),
            '1.2.3',
            'No version changes'
        );
        Test.assert.equal(
            vm('1.2.3.d').release(),
            '1.2.3',
            'No version changes'
        );
        Test.assert.equal(
            vm('1').release(),
            '1.0.0',
            'Default minor version is 0'
        );
        Test.assert.equal(vm('1.1').release(), '1.1.0', 'Default patch is 0');
    });

    it('Major releases tests', () => {
        Test.assert.equal(vm().major().release(), '1.0.0');
        Test.assert.equal(vm('1.2.3').major().release(), '2.0.0');
        Test.assert.equal(vm('1.2.3').major().major().release(), '3.0.0');
    });

    it('Minor releases tests', () => {
        Test.assert.equal(vm().minor().release(), '0.1.0');
        Test.assert.equal(vm('1.2.3').minor().release(), '1.3.0');
        Test.assert.equal(vm('1').minor().release(), '1.1.0');
        Test.assert.equal(vm('4').minor().minor().release(), '4.2.0');
    });

    it('Patch releases tests', () => {
        Test.assert.equal(vm().patch().release(), '0.0.2');
        Test.assert.equal(vm('1.2.3').patch().release(), '1.2.4');
        Test.assert.equal(vm('4').patch().patch().release(), '4.0.2');
    });

    it('Rollbacks tests', () => {
        Test.assert.equal(vm().major().rollback().release(), '0.0.1');
        Test.assert.equal(
            vm().major().major().major().minor().rollback().release(),
            '3.0.0'
        );
        Test.assert.equal(vm().minor().rollback().release(), '0.0.1');
        Test.assert.equal(vm().patch().rollback().release(), '0.0.1');
        Test.assert.equal(vm().major().patch().rollback().release(), '1.0.0');
        Test.assert.equal(
            vm().major().patch().rollback().major().rollback().release(),
            '1.0.0'
        );
    });

    it('Seperated calls', () => {
        const m = vm('1.2.3');
        m.major();
        m.minor();
        Test.assert.equal(m.release(), '2.1.0');
    });

    it('Exception tests', () => {
        const checkError = (fn, error) => {
            try {
                fn();
                Test.expect(false, 'An error should be thrown');
            } catch (e) {
                Test.expect(e instanceof Error);
                Test.assert.equal(e.message, error);
            }
        };

        checkError(() => {
            vm('a.b.c');
        }, 'Error occured while parsing version!');
        checkError(() => {
            vm().rollback();
        }, 'Cannot rollback!');
    });
});
